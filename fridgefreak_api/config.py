from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class GlobalConfig(BaseConfig):
    DB_FORCE_ROLL_BACK: bool = False
    DATABASE_HOST: Optional[str] = None
    DATABASE_USER: Optional[str] = None
    DATABASE_PASSWORD: Optional[str] = None
    DATABASE_PORT: Optional[int] = None
    DATABASE_NAME: Optional[str] = None
    TABLE_NAME: Optional[str] = None

class DevConfig(GlobalConfig):
    CLEVER_CLOUD_HOST: Optional[str] = None
    CLEVER_CLOUD_USER: Optional[str] = None
    CLEVER_CLOUD_PASSWORD: Optional[str] = None
    CLEVER_CLOUD_DB: Optional[str] = None
    
    model_config = SettingsConfigDict(env_prefix="DEV_")


class ProdConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="PROD_")


class TestConfig(GlobalConfig):

    model_config = SettingsConfigDict(env_prefix="TEST_")

@lru_cache()
def get_config(env_state: str):
    configs = {"dev": DevConfig, "prod": ProdConfig, "test": TestConfig}
    return configs[env_state]()

config = get_config(BaseConfig().ENV_STATE)