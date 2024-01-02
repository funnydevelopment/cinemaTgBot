import asyncio
import logging

from common.create_bot import bot, dp
from database.crud import create_movie_request_table, create_user_table
from src.handlers import router
from common.exceptions import MovieRequestCreateError, UserCreateError


logger = logging.getLogger(__name__)


async def run_bot() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    try:
        await create_movie_request_table()
        logger.info("Movie request table created successfully")
    except MovieRequestCreateError as error:
        logger.error("Error creating movie request table: %s", error)

    try:
        await create_user_table()
        logger.info("User table created successfully")
    except UserCreateError as error:
        logger.error("Error creating user table: %s", error)

    dp.include_router(router)

    logger.info("Bot is running")

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
