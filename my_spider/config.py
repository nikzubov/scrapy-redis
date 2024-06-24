from pydantic_settings import BaseSettings, SettingsConfigDict


# Класс для доступа к переменным окружения
class Settings(BaseSettings):
    R_PASSWORD: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
