import logging
import os

import aiosqlite

from common.exceptions import (
    MovieRequestAddError,
    UserAddError,
    SelectMovieRequestError,
    CountMovieRequestError,
)


logger = logging.getLogger(__name__)

db_file_path = os.path.join(os.path.dirname(__file__), "cinemadb.db")

DATABASE_URL = db_file_path


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
                (telegram_user_id,),
            )
            await db.commit()
            return True
        except UserAddError as error:
            logger.exception("Error adding user: %s", error)
        return False


async def get_history(telegram_user_id: str):
    async with aiosqlite.connect(DATABASE_URL) as db:
        try:
            cursor = await db.execute(
                """
                SELECT * FROM movie_request
                WHERE telegram_user_id = ?
                """,
                (telegram_user_id,),
            )
            rows = await cursor.fetchall()
            return rows
        except SelectMovieRequestError as error:
            logger.exception("Error selecting movie requests: %s", error)
        return


async def get_history_count(telegram_user_id: str):
    async with aiosqlite.connect(DATABASE_URL) as db:
        try:
            cursor = await db.execute(
                """
                SELECT COUNT(*) FROM movie_request
                WHERE telegram_user_id = ?
                """,
                (telegram_user_id,),
            )
            count = await cursor.fetchone()
            return count[0] if count else 0
        except CountMovieRequestError as error:
            logger.exception("Error counting movie requests: %s", error)
            return 0
