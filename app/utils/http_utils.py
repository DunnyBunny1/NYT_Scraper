import requests as reqs
import time
import logging

import requests.exceptions

# Init and configure logger
log: logging.Logger = logging.getLogger(__name__)


def make_http_req(req: reqs.Request, session: reqs.Session, retry_count=3):
    """
    Sends the given http request using the given session with retries,
    returning the json-formatted response content upon success and raising an
    error upon failure.

    :param req: The Request object to send, must be unprepared.
    :param session: The Request session through which to send the request.
    :param retry_count: The number of times to re-attempt the req, default=3.

    :return: The JSON response content as a python dictionary.

    :raises InvalidURL: If the URL is unknown.
    :raises TooManyRedirects: If max retries are reached.
    :raises RequestException: For unknown request errors.
    """

    try:
        while retry_count > 0:
            log.info(f"Sending {req.method} request...")
            # Prepare and send the request
            response = session.send(req.prepare())

            if response.status_code in (400, 404):
                raise reqs.exceptions.InvalidURL(
                    f"Bad request: client error or mal-formatted URL")
            elif response.status_code == 401:
                raise reqs.exceptions.HTTPError(
                    "Invalid auth token, or auth token does not have "
                    "permission for requested URL"
                )
            elif response.status_code == 429:  # Indicates too many requests
                retry_count -= 1
                log.warning(f"Too many requests. Retrying in 10 seconds...")
                # Sleep for 10 seconds before making a new request
                time.sleep(10)
            elif response.status_code != 200:  # Indicates some unknown error
                raise reqs.exceptions.RequestException(
                    f"Error with status code {response.status_code} encountered"
                )
            else:  # If we are here, we made a successful request
                log.info(f"Got successful response with code 200")
                return response.json()
        # If we are here, we ran out of retries
        raise reqs.exceptions.TooManyRedirects(
            f"Reached maximum retries for url."
        )

    except requests.exceptions.RequestException as e:
        log.error(f"Request error: {e}")
        raise e
