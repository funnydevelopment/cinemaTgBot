import logging

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from common.create_bot import api_client
from common.exceptions import (
    AddUserError,
    AddMovieRequestError,
    SelectMovieRequestError,
    CountMovieRequestError,
)
from database import crud as db
from .states import CinemaBotState
from . import text_messages as texts
from . import keyboards as kb
from . import utils


router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    user_id, user_fullname = message.from_user.id, message.from_user.full_name
    try:
        # todo: sql insert does not work
        user_insert = await db.add_user(telegram_user_id=str(user_id))
        if user_insert:
            logger.info("The user successfully recorded.")
        else:
            logger.info("Failed record the user.")
    except AddUserError as error:
        logger.error("Failed to record the client in the database; %s", error)
    finally:
        await message.answer(
            text=texts.HELLO_TEXT.format(user_name=user_fullname),
            reply_markup=kb.make_main_menu_kb(),
        )
        await state.set_state(state=CinemaBotState.main_state)


@router.message(Command("help"))
async def help_command(message: types.Message, state: FSMContext):
    await message.answer(text=texts.HELP_TEXT, reply_markup=kb.make_main_menu_kb())
    await state.set_state(state=CinemaBotState.main_state)


@router.message(Command("stats"))
async def stats_command(message: types.Message, state: FSMContext):
    user_name, telegram_user_id = message.from_user.full_name, message.from_user.id
    has_count = 0
    try:
        has_count = await db.get_history_count(telegram_user_id=str(telegram_user_id))
        if has_count:
            logger.info("The movie history successfully selected.")
        else:
            logger.info("Failed select the movie history.")
    except CountMovieRequestError as error:
        logger.exception("Error counting movie requests: %s", error)
    await message.answer(
        text=texts.STATS_TEXT.format(total_count=has_count),
        reply_markup=kb.make_main_menu_kb(),
    )
    await state.set_state(state=CinemaBotState.main_state)


@router.message(Command("history"))
async def history_command(message: types.Message, state: FSMContext):
    user_name, telegram_user_id = message.from_user.full_name, message.from_user.id
    has_history = ""
    # todo: rewrite exception class
    try:
        has_history = await db.get_history(telegram_user_id=str(telegram_user_id))
        if has_history:
            logger.info("The movie history successfully selected.")
        else:
            logger.info("Failed select the movie history.")
    except SelectMovieRequestError as error:
        logger.exception("Error selecting movie requests: %s", error)
    movie_list = await utils.create_movie_list(has_history)
    title_text = texts.HISTORY_TEXT.format(user_name=user_name)
    text = title_text + movie_list
    await message.answer(
        text=text,
        reply_markup=kb.make_main_menu_kb(),
    )
    await state.set_state(state=CinemaBotState.main_state)


@router.message(F.text.lower() == "instructions")
async def instruction_command(message: types.Message, state: FSMContext):
    await help_command(message, state)
    await state.set_state(state=CinemaBotState.main_state)


@router.message(F.text.lower() == "stats")
async def statistic_command(message: types.Message, state: FSMContext):
    await stats_command(message, state)
    await state.set_state(state=CinemaBotState.main_state)


@router.message(F.text.lower() == "history")
async def history_button_command(message: types.Message, state: FSMContext):
    await history_command(message, state)
    await state.set_state(state=CinemaBotState.main_state)


@router.message()
async def search_movie(message: types.Message, state: FSMContext):
    user_id, movie_name = message.from_user.id, message.text
    try:
        # todo: rewrite exception class
        movie_insert = await db.add_movie_request(
            name=movie_name, telegram_user_id=str(user_id)
        )
        if movie_insert:
            logger.info("The movie name successfully recorded.")
        else:
            logger.info("Failed record the movie name.")
    except AddMovieRequestError as error:
        logger.error("Failed to record the movie request in the database; %s", error)
    finally:
        search_result = await api_client.fetch_movie(query=movie_name)
        if search_result:
            await message.answer(
                text=texts.SEARCH_RESULT_TEXT.format(
                    name=search_result["title"],
                    rating=search_result["rating"],
                    overview=search_result["overview"],
                    link=search_result["movie_link"],
                ),
                reply_markup=kb.make_main_menu_kb(),
            )
            await state.set_state(state=CinemaBotState.main_state)
        else:
            await message.answer(
                text=texts.FAILED_RESULT_TEXT, reply_markup=kb.make_main_menu_kb()
            )
            await state.set_state(state=CinemaBotState.main_state)
