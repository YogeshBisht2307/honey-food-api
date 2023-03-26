from pydantic import BaseSettings

class Settings(BaseSettings):
    key_json_data: str

    class Config:
        env_file = ".env"