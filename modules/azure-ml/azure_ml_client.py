from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import mlflow


class AzureClient:
    def __init__(self, subscription_id: str, ressource_group: str, workspace_name: str):
        self.ml_client = MLClient(
            credential=DefaultAzureCredential(),
            subscription_id=subscription_id,
            resource_group_name=ressource_group,
            workspace_name=workspace_name
        )

        self.azure_ml_tracking_uri = self.ml_client.workspaces.get(self.ml_client.workspace_name).mlflow_tracking_uri

    def set_experiment_to_log_to_azure(self, experiment_name: str):
        mlflow.set_tracking_uri(self.azure_ml_tracking_uri)
        mlflow.set_experiment(experiment_name)
