from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    BOT_TOKEN: str


@dataclass
class HTTPClient:
    API_URL: str
    API_KEY: str
    API_TOKEN: str


@dataclass
class Config:
    tg_bot: TgBot
    http_client: HTTPClient


def load_config(path: str) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(BOT_TOKEN=env.str("BOT_TOKEN")),
        http_client=HTTPClient(
            API_URL=env.str("API_URL"),
            API_KEY=env.str("API_KEY"),
            API_TOKEN=env.str("API_TOKEN"),
        ),
    )
