from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
import os


class Config(BaseSettings):
    # Azure Foundry

    # Azure ML
    azure_subscription_id: str = "234a32e8-6f2e-47f8-8940-6204931f5ff5"
    azure_resource_group: str = "rg_aifoundry_swe1"
    azure_workspace_name: str = "wgg-swe-aml-ds"
    azure_experiment_name: str = "ml-contracts-kommunikation"


    # Load Environment
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), "..", ".env"), extra="ignore")
