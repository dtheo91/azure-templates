from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
import os


class Config(BaseSettings):
    # Azure Foundry

    # Azure ML
    azure_subscription_id: str = ""
    azure_resource_group: str = ""
    azure_workspace_name: str = ""
    azure_experiment_name: str = ""


    # Load Environment
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), "..", ".env"), extra="ignore")
