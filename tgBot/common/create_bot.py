from aiogram import Bot, Dispatcher

from .config import Config, load_config
from .services import MovieAPIClient

config: Config = load_config(".env")
bot: Bot = Bot(token=config.tg_bot.BOT_TOKEN, parse_mode="HTML")
dp: Dispatcher = Dispatcher()
api_client = MovieAPIClient(
    api_url=config.http_client.API_URL,
    api_key=config.http_client.API_KEY,
    api_token=config.http_client.API_TOKEN,
    movie_url=config.http_client.MOVIE_URL,
)
