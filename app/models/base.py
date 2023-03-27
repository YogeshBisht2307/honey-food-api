from pydantic import BaseModel, Field, BaseSettings


class ResponseOut(BaseModel):
    code: str = Field(title="Code")
    message: str = Field(title="Message")

class Settings(BaseSettings):
    KEY_JSON_DATA: str
    X_HONEY_FOOD_API_KEY: str
    X_API_USER_INFO: str
    STAGE: str

    class Config:
        env_file = ".env"

settings = Settings()
