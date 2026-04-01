from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    HOPSWORKS_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

RAW_DATA_PATH = DATA_DIR / "raw" / "Titanic-Dataset.csv"
PROCESSED_DATA_PATH = DATA_DIR / "processed" / "titanic_features.csv"
DAILY_DATA_PATH = DATA_DIR / "processed" / "daily_features.csv"

MODELS_DIR = BASE_DIR / "models"
MODEL_PATH = MODELS_DIR / "titanic_model.pkl"

OUTPUTS_DIR = BASE_DIR / "outputs"
IMAGES_DIR = MODELS_DIR / "images"