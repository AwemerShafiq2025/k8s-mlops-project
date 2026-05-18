import kfp
from kfp import dsl
from kfp.compiler import Compiler

# Component 1: Data Preparation
@dsl.component(
    base_image='python:3.9-slim',
    packages_to_install=['pandas', 'scikit-learn']
)
def prepare_data() -> str:
    from sklearn.datasets import load_iris
    import pandas as pd
    import json
    
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    return json.dumps(df.to_dict(orient='list'))

# Component 2: Model Training
@dsl.component(
    base_image='python:3.9-slim',
    packages_to_install=['pandas', 'scikit-learn']
)
def train_model(data_json: str) -> str:
    import json
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    import pickle
    import codecs
    
    data = json.loads(data_json)
    df = pd.DataFrame(data)
    
    X = df.drop(columns=['target'])
    y = df['target']
    
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    
    model_serialized = codecs.encode(pickle.dumps(model), "base64").decode("utf-8")
    return model_serialized

# Component 3: Model Evaluation
@dsl.component(
    base_image='python:3.9-slim',
    packages_to_install=['pandas', 'scikit-learn']
)
def evaluate_model(data_json: str, model_str: str) -> float:
    import json
    import pandas as pd
    import pickle
    import codecs
    
    data = json.loads(data_json)
    df = pd.DataFrame(data)
    
    X = df.drop(columns=['target'])
    y = df['target']
    
    model = pickle.loads(codecs.decode(model_str.encode("utf-8"), "base64"))
    accuracy = float(model.score(X, y))
    print(f"\n=====================================")
    print(f"  SUCCESS: Model Accuracy: {accuracy * 100}%")
    print(f"=====================================\n")
    return accuracy

# Defining the Kubeflow Pipeline Flow
@dsl.pipeline(
    name='iris-mlops-pipeline',
    description='A clean pipeline to load, train and evaluate Iris model for university submission.'
)
def iris_mlops_pipeline():
    data_task = prepare_data()
    train_task = train_model(data_json=data_task.output)
    eval_task = evaluate_model(data_json=data_task.output, model_str=train_task.output)

if __name__ == '__main__':
    # 1. Compiling for Sir's requirement (Generates the iris_pipeline.yaml)
    Compiler().compile(
        pipeline_func=iris_mlops_pipeline,
        package_path='iris_pipeline.yaml'
    )
    print("1. Success: iris_pipeline.yaml has been generated for submission!")
    
    # 2. Local Simulation (Runs the pipeline steps locally to get results immediately)
    print("2. Running local execution pipeline simulation...")
    from kfp.local import init, SubprocessRunner
    init(runner=SubprocessRunner())
    iris_mlops_pipeline()
