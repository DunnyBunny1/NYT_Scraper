from services.nyt_api_client import NytApiClient
import logging
from typing import List
from config.logging_config import setup_logging
from models.top_stories_models import Article

setup_logging()
log = logging.getLogger(__name__)


def main():
    nyt_api_client: NytApiClient = NytApiClient()
    articles: List[Article] = nyt_api_client.pull_top_stories(section="sports")
    log.info(f'Article list: {articles}')
    for idx, article in enumerate(articles):
        log.info(f"Article #{idx + 1}: Title: {article.title}")

# for idx, story in enumerate(top_stories_json["results"]):
#     log.info(f"Article #{idx + 1}: Title: {story['title']}")


if __name__ == "__main__":
    main()
