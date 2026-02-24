import discord
from discord.ext import commands

class Interface(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# load_extension()에서 호출
async def setup(bot):
    await bot.add_cog(Interface(bot))