import logging

from common.http_client import HTTPRequestMaker

logger = logging.getLogger(__name__)


class MovieAPIClient:
    http = HTTPRequestMaker()

    def __init__(self, api_url: str, api_key: str, api_token: str):
        self.api_url = api_url
        self.api_key = api_key
        self.api_token = api_token

    async def fetch_movie(self, query: str) -> dict:
        url = f"{self.api_url}"
        params = {
            "query": query,
            "api_key": self.api_key,
        }
        response = await self.http.get(url=url, params=params)
        parsed_data = await self.data_parse(response["results"])
        print(parsed_data)
        return parsed_data

    @staticmethod
    async def data_parse(url_response) -> dict:
        parsed_data = dict()
        try:
            parsed_data["id"] = url_response[0]["id"]
            parsed_data["title"] = url_response[0]["original_title"]
            parsed_data["overview"] = url_response[0]["overview"]
            parsed_data["poster"] = url_response[0]["poster_path"]
            parsed_data["rating"] = url_response[0]["vote_average"]
        except KeyError as error:
            logger.error("Can't retrieve first element from result: %s", error)
        return parsed_data
