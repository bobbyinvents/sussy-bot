from dotenv import load_dotenv
from discord.ext import commands

import asyncio
import discord
import os
import random

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    status = "DM me about your day! \N{YELLOW HEART}"
    await bot.change_presence(activity=discord.Game(name=status))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_greetings = ["hi", "hello", "hey"]
    news_stories = [
        "abcnews.go.com",
        "bbc.co.uk",
        "bbc.com",
        "cnn.com",
        "foxnews.com",
        "huffpost.com",
        "usatoday.com",
        "nbcnews.com",
        "nytimes.com",
        "telegraph.co.uk",
        "theguardian.com",
        "washingtonpost.com",
    ]
    catchphrase_pieces = [
        "haha",
        "yea",
        "oh",
        "dang",
        "*Noice*",
        "thanks",
        "hmm",
        ":rofl:",
        "hecc",
    ]

    if "zech" in message.content.lower():
        bot_reply = "haha zech too smart"
    elif any(phrase in message.content.lower() for phrase in user_greetings):
        bot_reply = "howdy"
    elif any(link in message.content.lower() for link in news_stories):
        bot_reply = "what in tarnation"
    else:
        bot_reply = " ".join(
            random.choices(
                catchphrase_pieces,
                weights=[10, 5, 2, 9, 6, 2, 1, 7, 1],
                k=random.randrange(1, 4),
            )
        )

    await message.author.send(bot_reply)


load_dotenv()
token = os.getenv("TOKEN")
bot.run(token)
