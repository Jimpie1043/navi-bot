import discord
from discord.ext import commands

import os
from os import listdir
from dotenv import load_dotenv
from ruamel.yaml import YAML
from pathlib import Path
import logging
import asyncio

from app.config.config import Config

#FIXME: Import and use events/utils correctly.

load_dotenv()

config_path = Path('app/config/config.yml')
yaml = YAML(typ='safe')
config = yaml.load(config_path)

# Message_content intent is needed for the bot to function, so it needs to be on regardless of configuration.
intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config['Prefix']), intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

async def load_extensions():
    print("------------- Loading -------------")
    for file in listdir("./app/cogs"):
        if file.endswith(".py") and file != '__init__.py':
            print(f"Loading: {file}")
            await bot.load_extension(f"app.cogs.{file[:-3]}")
            print(f"Loaded {file}")
    print("------------- Finished Loading -------------")

# FIXME: Cogs not properly being loaded (some issues with async and await...)
if __name__ == '__main__':
    asyncio.run(load_extensions())

    token = os.getenv('TOKEN')
    bot.run(token)