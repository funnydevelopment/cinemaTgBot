import logging

from common.http_client import HTTPRequestMaker

logger = logging.getLogger(__name__)


class MovieAPIClient:
    http = HTTPRequestMaker()

    def __init__(self, api_url: str, api_key: str, api_token: str, movie_url: str):
        self.api_url = api_url
        self.api_key = api_key
        self.api_token = api_token
        self.movie_url = movie_url

    async def fetch_movie(self, query: str) -> dict:
        url = f"{self.api_url}"
        params = {
            "query": query,
            "api_key": self.api_key,
        }
        response = await self.http.get(url=url, params=params)
        parsed_data = await self.data_parse(response["results"])
        return parsed_data

    async def data_parse(self, url_response) -> dict | None:
        parsed_data = dict()
        try:
            parsed_data["title"] = url_response[0]["original_title"]
            parsed_data["overview"] = url_response[0]["overview"]
            parsed_data["poster"] = url_response[0]["poster_path"]
            parsed_data["rating"] = url_response[0]["vote_average"]
            parsed_data["movie_link"] = f'{self.movie_url}{url_response[0]["id"]}'
        except IndexError as error:
            logger.error("Can't retrieve first element from result: %s", error)
            return
        except KeyError as error:
            logger.error("Can't retrieve first element from result: %s", error)
            return
        return parsed_data
