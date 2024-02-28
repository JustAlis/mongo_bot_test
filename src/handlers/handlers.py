from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router
from utils import parse_input, fill_missing_values
from mongo import get_db_values
from replies import on_start, wrong_attrs, wrong_input

router: Router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text=on_start)

@router.message()
async def main_handler(message: Message):
    try:
        aggregation_type, dt_from, dt_upto = parse_input(message.text)
    except:
        await message.answer(text=wrong_input)
        return
    
    try:
        dataset, lables = await get_db_values(aggregation_type, dt_from, dt_upto)
        result = fill_missing_values(dataset, lables, dt_from, dt_upto, aggregation_type)
        await message.answer(text=result)
    except:
        await message.answer(text=wrong_attrs)

