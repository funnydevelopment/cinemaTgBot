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
        text=texts.HELP_TEXT.format(user_name=user_fullname),
        reply_markup=kb.make_main_menu_kb(),
    )
    await state.set_state(state=CinemaBotState.main_state)


@router.message(Command("help"))
async def help_command(message: types.Message, state: FSMContext):
    await message.answer(text=texts.HELP_TEXT, reply_markup=kb.make_main_menu_kb())
    await state.set_state(state=CinemaBotState.main_state)


@router.message(F.text.lower() == "инструкция")
async def instruction_command(message: types.Message, state: FSMContext):
    await help_command(message, state)
    await state.set_state(state=CinemaBotState.main_state)
