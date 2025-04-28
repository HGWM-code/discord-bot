import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

# Cogs laden
async def load_extensions():
    await bot.load_extension("commands.greeting") 

@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())
