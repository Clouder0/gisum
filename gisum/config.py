from dataclasses import dataclass
from dotenv import dotenv_values, load_dotenv

env_values = dotenv_values(".env")


@dataclass
class Config:
    api_key: str
    base_url: str


config = Config(
    api_key=env_values["API_KEY"],
    base_url=env_values.get("BASE_URL", "https://api.openai.com"),
)
