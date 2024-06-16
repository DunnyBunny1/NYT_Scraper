import os
from dotenv import load_dotenv
from dataclasses import dataclass
# Load environment variables 
load_dotenv()

@dataclass
class Config():
    nyt_api_key : str = os.getenv('API_KEY')
    top_stories_base_url : str = os.getenv('TOP_STORIES_BASE_URL')