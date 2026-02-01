from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

class AzureFoundryClient:
    def __init__(self, user_endpoint: str):
        self.project_client = AIProjectClient(
            endpoint=user_endpoint,
            credential=DefaultAzureCredential(),
        )

        self.openai_client = self.project_client.get_openai_client()