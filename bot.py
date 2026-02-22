import os, discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
from pytz import timezone

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = 1473674730212032685

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

async def load_extensions():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            extension = 'cogs.' + filename[:-3]
            print(f"{extension} 모듈을 불러왔습니다.")
            await bot.load_extension(extension)

@bot.event
async def on_ready():

    print("Hi, logged in as ", end="")
    print(bot.user.name)
    print()

@bot.event
async def setup_hook():
    await load_extensions()
    await bot.tree.sync()

bot.run(TOKEN)
