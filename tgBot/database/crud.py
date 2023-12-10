import logging

import aiosqlite

from common.exceptions import MovieRequestAddError, UserAddError


logger = logging.getLogger(__name__)

DATABASE_URL = "cinemadb.db"


async def create_movie_request_table() -> None:
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS movie_request (
                id INTEGER PRIMARY KEY,
                name TEXT,
                telegram_user_id TEXT
            )
        """
        )
        await db.commit()


async def create_user_table() -> None:
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS telegram_user (
                id INTEGER PRIMARY KEY,
                telegram_user_id TEXT
            )
        """
        )
        await db.commit()


async def add_movie_request(name: str, telegram_user_id: str) -> bool:
    async with aiosqlite.connect(DATABASE_URL) as db:
        try:
            await db.execute(
                """
                INSERT INTO movie_request (name, telegram_user_id)
                VALUES (?, ?)
            """,
                (name, telegram_user_id),
            )
            await db.commit()
            return True
        except MovieRequestAddError as error:
            logger.exception("Error adding movie request: %s", error)
        return False


async def add_user(telegram_user_id: str) -> bool:
    async with aiosqlite.connect(DATABASE_URL) as db:
        try:
            await db.execute(
                """
                INSERT INTO telegram_user (telegram_user_id)
                VALUES (?)
            """,
                telegram_user_id,
            )
            await db.commit()
            return True
        except UserAddError as error:
            logger.exception("Error adding user: %s", error)
        return False
