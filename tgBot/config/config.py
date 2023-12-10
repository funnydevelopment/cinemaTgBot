from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    BOT_TOKEN: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(BOT_TOKEN=env.str("BOT_TOKEN")),
    )
