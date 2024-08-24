import logging
import pprint
from typing import Any, Dict, List
from functools import cached_property
import requests as reqs
from config.config import Config
from utils.http_utils import make_http_req
from models.top_stories_models import TopStoriesResponse, Article

# Init and configure logger
log: logging.Logger = logging.getLogger(__name__)


class NytApiClient:
    """
    A client for interacting with the various NYT public API endpoints.
    Encapsulates the `/topstories` V2 endpoint.
    """
    TOP_STORIES_BASE_URL = 'https://api.nytimes.com/svc/topstories/v2'

    def __del__(self):
        """
        When this client instance is garbage-collected from memory, closes
        its requests HTTP session.
        """
        self._session.close()

    @cached_property
    def _api_key(self) -> str:
        conf: Config = Config()
        return conf.nyt_api_key

    @cached_property
    def _session(self) -> reqs.Session:
        return reqs.Session()

    @staticmethod
    def _get_req_headers():
        return {
            "Content-Type": "application/json",
        }

    def _get_auth_param(self):
        return {"api-key": self._api_key}

    def pull_top_stories(self, section: str) -> List[Article]:
        """
        Pulls the top stories (articles) from the NYT API. Returns the result
        as a set of Article objects.
        """
        # Create a request to the top stories endpoint
        url = f"{NytApiClient.TOP_STORIES_BASE_URL}/{section}.json"
        headers = self._get_req_headers()
        params = self._get_auth_param()

        # Send the GET request and grab the response in JSON form
        req = reqs.Request(
            method='GET', url=url, headers=headers, params=params
        )
        response_json: Dict[str, Any] = make_http_req(req, self._session)
        validated_response = TopStoriesResponse(**response_json)

        log.info("\n" + pprint.pformat(response_json))

        return validated_response.results
