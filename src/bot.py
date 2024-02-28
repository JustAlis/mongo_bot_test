import asyncio
from aiogram import Bot, Dispatcher
from config import conf
import handlers

async def main():
    bot = Bot(token = conf.token)
    dp = Dispatcher(bot=bot)
    dp.include_router(handlers.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")