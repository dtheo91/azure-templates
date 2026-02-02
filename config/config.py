from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
import os


class Config(BaseSettings):
    # Azure Foundry
    azure_foundry_endpoint: str
    azure_foundry_openai_endpoint: str
    azure_foundry_api_key: SecretStr

    # Azure ML
    azure_subscription_id: str
    azure_resource_group: str
    azure_workspace_name: str
    azure_experiment_name: str

    # Azure Document Intelligence
    azure_document_intelligence_endpoint: str


    # Load Environment
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), "..", ".env"), extra="ignore")
