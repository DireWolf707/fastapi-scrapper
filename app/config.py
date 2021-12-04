from pydantic import BaseSettings,Field
from functools import lru_cache
import os

if os.getenv("CQLENG_ALLOW_SCHEMA_MANAGEMENT") is None :
    os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT']="1"

class Settings(BaseSettings):
    name : str = Field(...,env="PROJ_NAME")
    client_id : str = Field(...,env='ASTRA_CLIENT_ID')
    client_secret : str = Field(...,env='ASTRA_CLIENT_SECRET')

    class Config:
        env_file = '.env'

@lru_cache
def get_settings():
    return Settings()