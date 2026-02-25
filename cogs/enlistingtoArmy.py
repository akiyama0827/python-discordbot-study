import discord, sqlite3
from discord import app_commands
from discord.ext import commands
from db import db

class EnlistingtoArmy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='병역정보등록', description="군생활 정보를 등록합니다.")
    @app_commands.describe(입대일="입영일자(ex: 250819)", 전역일="전열일자(ex: 270218", 군별="육군/공군/해군")
    async def mili_register(self, interaction: discord.Interaction, 입대일: str, 전역일: str, 군별: str):
        user_id = interaction.user.id
        enlistment_date = f"20{입대일[0:2]}-{입대일[2:4]}-{입대일[4:6]}"
        discharge_date = f"20{전역일[0:2]}-{전역일[2:4]}-{전역일[4:6]}"
        branch = 군별
        try: # 플레이어 등록 시도
            db.execute("INSERT INTO player (user_id, enlistment_date, discharge_date, branch) VALUES (?, ?, ?, ?)", user_id, enlistment_date, discharge_date, branch)
            await interaction.response.send_message("병역정보가 등록되었습니다.")
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                await interaction.response.send_message("이미 등록된 사용자입니다.")
            else:
                await interaction.response.send_message(f"등록 중에 오류가 발생했습니다: {e}")
        
async def setup(bot):
    await bot.add_cog(Player(bot))