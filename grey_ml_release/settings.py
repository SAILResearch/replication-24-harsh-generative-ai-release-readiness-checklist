from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    # Google custom search JSON API settings
    SERP_API_KEY: str = Field(..., env="SERP_API_KEY")

    COMPANIES: list[str] = [
        "openai",
        "google",
        "deepmind",
        "huawei",
        "nvidia",
        "microsoft",
        "baidu",
        "meta",
        "amazon",
        "ibm",
    ]

    RUN_DIR: Path = Path(__file__).parent.parent / "run"
    # Path to the directory where the data will be stored
    DATA_DIR: Path = RUN_DIR / "data"
    # Path to the directory where the results will be stored
    RESULTS_DIR: Path = RUN_DIR / "results"

    SEARCH_STRING: str = (
        """("generative ai" | "large language models" | llms | "foundation models" | chatgpt | "conversational ai") AND (release | production | deployment | monitoring | observability | operations) AND (checklist | checks | guardrails | considerations | requirements | practices | patterns | challenges | methods | risks)"""
    )

    ENGINE: str = "google"


settings = Settings()
