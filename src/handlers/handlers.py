from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router
from utils import parse_input
from mongo import get_db_values

router: Router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.reply(text="ready")

@router.message()
async def main_handler(message: Message):
    aggregation_type, dt_from, dt_upto = parse_input(message.text)
    dataset, lables = get_db_values(aggregation_type, dt_from, dt_upto)
    print(dataset)
    print(lables)
    await message.reply(text=message.text)
