FROM jenkins/jenkins:2.492.3-alpine
RUN jenkins-plugin-cli --plugins git github pipeline-stage-view credentials-binding
