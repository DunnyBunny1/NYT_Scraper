import os
from dotenv import load_dotenv
from functools import cached_property

class Config:
    """
    Configuration class to load environment variables and provide access to
    necessary configuration settings like API keys and URLs.
    """

    def __init__(self) -> None:
        """
        Initializes the Config class and load environment variables from .env
        file.
        """
        load_dotenv()

    @cached_property
    def nyt_api_key(self) -> str:
        """
        Fetches the NYT API key from the environment and ensures it's present and not empty.

        Returns:
            str: The NYT API key.
        Raises:
            ValueError: If the NYT API key is not found or is an invalid string.
        """
        nyt_api_key: str = os.getenv("API_KEY", "").strip()
        if not nyt_api_key:
            raise ValueError("NYT API Key is missing, empty, or invalid string")
        return nyt_api_key
