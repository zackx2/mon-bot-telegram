import os
import snscrape.modules.twitter as sntwitter
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio

BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = -2424886189

TWITTER_USER = 'FabrizioRomano'
FOOTMERCATO_URL = 'https://www.footmercato.net/'

bot = Bot(token=BOT_TOKEN)

async def scrape_twitter():
    last_tweet = next(sntwitter.TwitterUserScraper(TWITTER_USER).get_items())
    tweet_text = last_tweet.content
    reformulated = f"{tweet_text}"
    await bot.send_message(chat_id=CHANNEL_ID, text=reformulated)

async def scrape_footmercato():
    response = requests.get(FOOTMERCATO_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    title_tag = soup.find('h2')
    if title_tag:
        title = title_tag.get_text().strip()
        reformulated = f"{title}"
        await bot.send_message(chat_id=CHANNEL_ID, text=reformulated)

async def main():
    while True:
        await scrape_twitter()
        await scrape_footmercato()
        await asyncio.sleep(300)

asyncio.run(main())
