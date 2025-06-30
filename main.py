import os
import asyncio
import snscrape.modules.twitter as sntwitter
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)

async def main():
    tweet = next(sntwitter.TwitterUserScraper('FabrizioRomano').get_items())
    text = tweet.content.split('.')[0]
    await bot.send_message(chat_id=CHANNEL_ID, text=text)

if __name__ == "__main__":
    asyncio.run(main())
