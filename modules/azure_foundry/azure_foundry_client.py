from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import OpenAI
from pydantic import SecretStr

class AzureFoundryClient:
    def __init__(self, user_endpoint: str, openai_endpoint: str, api_key: SecretStr):
        self.project_client = AIProjectClient(
            endpoint=user_endpoint,
            credential=DefaultAzureCredential(),
        )

        self.openai_client = self.project_client.get_openai_client()
        self.model_client = OpenAI(base_url=openai_endpoint, api_key=api_key.get_secret_value())

    def get_embeddings(self, text_list: list, model_deployment_name: str):
        """Generates vectors for a list of text strings."""
        response = self.model_client.embeddings.create(input=text_list, model=model_deployment_name)
        return [item.embedding for item in response.data]