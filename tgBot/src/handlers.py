import logging

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .states import CinemaBotState
from . import text_messages as texts
from . import keyboards as kb


router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    user_id, user_fullname = message.from_user.id, message.from_user.full_name
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
    await message.answer(
        text=texts.STATS_TEXT.format(user_name=user_name),
        reply_markup=kb.make_main_menu_kb()
    )
    await state.set_state(state=CinemaBotState.main_state)


@router.message(Command("history"))
async def history_command(message: types.Message, state: FSMContext):
    user_name, telegram_user_id = message.from_user.full_name, message.from_user.id
    await message.answer(
        text=texts.HISTORY_TEXT.format(user_name=user_name),
        reply_markup=kb.make_main_menu_kb()
    )
    await state.set_state(state=CinemaBotState.main_state)


@router.message(F.text.lower() == "инструкция")
async def instruction_command(message: types.Message, state: FSMContext):
    await help_command(message, state)
    await state.set_state(state=CinemaBotState.main_state)


@router.message(F.text.lower() == "статистика")
async def statistic_command(message: types.Message, state: FSMContext):
    await stats_command(message, state)
    await state.set_state(state=CinemaBotState.main_state)


@router.message(F.text.lower() == "история")
async def story_command(message: types.Message, state: FSMContext):
    await history_command(message, state)
    await state.set_state(state=CinemaBotState.main_state)
