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
            await bot.load_extension(extension)
            print(f"{extension} 모듈을 불러왔습니다.")

@bot.event
async def on_ready():

    print("Hi, logged in as ", end="")
    print(bot.user.name)
    print()

@bot.event
async def setup_hook():
    await load_extensions()
    await bot.tree.sync()

@bot.command(name='unload')
@commands.is_owner()
async def unload(ctx, extension: str):
    try:
        await bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} Cog를 제거했습니다.')
    except Exception as e:
        await ctx.send(f'오류: {e}')

@bot.command(name='load')
@commands.is_owner()
async def unload(ctx, extension: str):
    try:
        await bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} Cog를 불러왔습니다.')
        await bot.tree.sync()
    except Exception as e:
        await ctx.send(f'오류: {e}')

@bot.command(name='reload')
@commands.is_owner()
async def reload(ctx, extension: str):
    try:
        await bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} Cog를 다시 불러왔습니다.')
        await bot.tree.sync()
    except Exception as e:
        await ctx.send(f'오류: {e}')

bot.run(TOKEN)
