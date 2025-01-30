import asyncio
from telegram import Bot
from decouple import config

async def test_token():
    token = config('TELEGRAM_TOKEN')
    bot = Bot(token=token)
    try:
        await bot.get_me()
        print("Token is valid and connection is successful.")
    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == "__main__":
    asyncio.run(test_token())
