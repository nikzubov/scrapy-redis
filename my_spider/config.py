from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс для доступа к переменным окружения"""
    R_PASSWORD: str

    model_config = SettingsConfigDict(env_file='my_spider/.env')


settings = Settings()
