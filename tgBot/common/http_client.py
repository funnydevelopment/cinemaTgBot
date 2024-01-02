import aiohttp

from common.exceptions import BadRequestError


class HTTPRequestMaker:
    @staticmethod
    async def get(url: str, params: dict):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, params=params) as response:
                if 200 <= response.status < 300:
                    return await response.json()
                if response.status == 400:
                    raise BadRequestError()
                raise ValueError(
                    f"Invalid response: {response.status}, {response.text}"
                )
