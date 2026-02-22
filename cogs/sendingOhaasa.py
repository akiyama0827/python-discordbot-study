import os, discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from dotenv import load_dotenv

import crawllingOhaasa
horo_text_list = crawllingOhaasa.horo_text_list

load_dotenv()
CHANNEL_LIST = os.getenv("OHAASA_CHANNEL")

# 오하아사 메시지 보내는 함수
# 표시해둔 줄은 특정 시간에 메시지를 보내는 함수이니 코드 테스트 시 수정할 것
class sendingOhaasa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @tasks.loop(minutes = 2)
    async def ohaasa_message():
        now = datetime.now(timezone('Asia/Seoul'))
        #if now.hour==7 and now.minute<=15: ### 테스트 시 조건 True로 수정
        if True:
        # update horo_text_list
            os.system("python3 crawllingOhaasa.py")

            embed = discord.Embed(
                title=datetime.strftime(now, '%Y년 %m월 %d일 오하아사 순위'),
                color=discord.Color.gold(),
                timestamp=now,
                url='https://www.asahi.co.jp/ohaasa/week/horoscope/'
            )
            for i in range(len(horo_text_list)):
                embed.add_field(name=f"{horo_text_list[i][0]}위- {horo_text_list[i][1]}",
                                value="",
                                inline=False)

            embed.set_author(name="오하아사 봇")
            embed.set_thumbnail(url='https://www.asahi.co.jp/ohaasa/week/horoscope/img/ttl_horoscope.png')

            for channel_id in CHANNEL_LIST:
                channel = bot.get_channel(channel_id)
                await channel.send(embed=embed, view=SelectView())

async def setup(bot):
    await bot.add_cog(sendingOhaasa(bot))