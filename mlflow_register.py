import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from mlflow.tracking import MlflowClient

def register_and_promote_model():
    # 1. Set tracking URI locally
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("Iris_University_Project")
    
    # 2. Re-log the successful model metrics for tracking
    with mlflow.start_run() as run:
        iris = load_iris()
        X, y = iris.data, iris.target
        
        model = LogisticRegression(max_iter=200)
        model.fit(X, y)
        accuracy = model.score(X, y)
        
        # Logging metrics and model
        mlflow.log_metric("accuracy", accuracy)
        print(f"Logging model to MLflow with accuracy: {accuracy * 100}%")
        
        # Registering the model directly
        model_info = mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="iris-model",
            registered_model_name="IrisK8sModel"
        )
        
    # 3. Transition Stage: Staging -> Production
    client = MlflowClient()
    model_name = "IrisK8sModel"
    
    # Latest version dhoondna
    latest_versions = client.get_latest_versions(model_name, stages=["None"])
    if latest_versions:
        current_version = latest_versions[0].version
        print(f"Latest Model Version Found: {current_version}")
        
        # Phase 5 Target: Move to Production
        client.transition_model_version_stage(
            name=model_name,
            version=current_version,
            stage="Production",
            archive_existing_versions=True
        )
        print(f"SUCCESS: Model Version {current_version} has been transitioned to PRODUCTION!")
    else:
        print("Error: Could not find registered model version.")

if __name__ == "__main__":
    register_and_promote_model()
