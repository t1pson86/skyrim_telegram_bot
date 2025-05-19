import asyncio
import os
from aiogram import Bot, Dispatcher


from app.handler.heandlers import router
from app.database.database import async_main




async def main():
    await async_main()
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')