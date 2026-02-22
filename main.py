# from selenium.webdriver.common import options
# from discord.app_commands.commands import describe
# 메시지 임베드로 전송하게끔 수정

import discord
from discord.ext import tasks

from datetime import datetime # timestamp 시간 확인용
from pytz import timezone

intents = discord.Intents.default()
intents.message_content = True

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_ID = 1473674730212032685

client = discord.Client(intents=intents)


import crawllingOhaasa
horo_text_list = crawllingOhaasa.horo_text_list

horo_emoji = {"양자리":"♈", "황소자리":"♉", "쌍둥이자리":"♊", "게자리":"♋",
              "사자자리":"♌", "처녀자리":"♍", "천칭자리":"♎", "전갈자리":"♏",
              "궁수자리":"♐", "염소자리":"♑", "물병자리":"♒", "물고기자리":"♓"}

horo_thubnails = {"양자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045297872339186/aries_8376955.png?ex=69986b29&is=699719a9&hm=9ed4dd64b850ae2ce9514f07713e8ca332b872805bdf6f1b0061dd97b2a5f6ef&=&format=webp&quality=lossless",
                  "황소자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045330973655184/taurus_8376965.png?ex=69986b31&is=699719b1&hm=21efa6387f69b888e50c9af24c03cccd08113c680fbfdefd079363dcad1b375d&=&format=webp&quality=lossless",
                  "쌍둥이자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045328494956696/gemini_8376976.png?ex=69986b30&is=699719b0&hm=8c229f65b49244de54c202381effe207b42cc9b2a2568c9140b0c04d3de3e0d4&=&format=webp&quality=lossless",
                  "게자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045298522198036/cancer_8376986.png?ex=69986b29&is=699719a9&hm=102cf5557624f7785f08cee5d7e91a77f88715f9fb1698b0faebfb56e0dfcac3&=&format=webp&quality=lossless",
                  "사자자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045329098801255/leo_8376996.png?ex=69986b30&is=699719b0&hm=d84db6d70d171d53c93202588898d1fb221022e247ad88ae9db2d64f81cb5f33&=&format=webp&quality=lossless",
                  "처녀자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045331296620637/virgo_8377008.png?ex=69986b31&is=699719b1&hm=5679fcdb23328d9dcb74f0587db42aa64a06b4d9e4776556ffb73d94acd3e666&=&format=webp&quality=lossless",
                  "천칭자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045329434349742/libra_8377019.png?ex=69986b30&is=699719b0&hm=bc3dc32461ac95607d424dac55a3d4bc45c25aa5f193799e8d7aa9341f780213&=&format=webp&quality=lossless",
                  "전갈자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045330600493116/scorpio_8377030.png?ex=69986b31&is=699719b1&hm=f70e84f2c26a675e76be72af1970b2461fb16893037364c1b234533c98d96c1b&=&format=webp&quality=lossless",
                  "궁수자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045330239520931/sagittarius_8377042.png?ex=69986b31&is=699719b1&hm=b90ec5f6885debf4492656e20f2290f9b519de728e513ac30908c8208b990aaa&=&format=webp&quality=lossless",
                  "염소자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045299096813733/capricorn_8377058.png?ex=69986b29&is=699719a9&hm=efe4d55150a5124140d324d1506b1dda101e13143cd998eb2e7772c390abd2fc&=&format=webp&quality=lossless",
                  "물병자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045297545056452/aquarius_8377070.png?ex=69986b29&is=699719a9&hm=4ce379c2a49221f9cefb814c77a1caa5a4d5f76b365bb6741f5b3ee8f5be2ae4&=&format=webp&quality=lossless",
                  "물고기자리":"https://media.discordapp.net/attachments/1474045106091987018/1474045329795190784/pisces_8377080.png?ex=69986b31&is=699719b1&hm=0e02a1e08edf573cc7bdd27f01cd333bbf098776dfe9ac929e86fbb2b8c73452&=&format=webp&quality=lossless"}

# 오하아사 순위 밑에 전송할 드롭다운 메뉴 UI
class SelectView(discord.ui.View):
    @discord.ui.select(
        placeholder="별자리를 선택하세요",
        min_values=1, # 골라야 할 최소 갯수
        max_values=1, # 고를 수 있는 최대 갯수
        options=[
            discord.SelectOption(
                label=f"{horo_text_list[i][0]}. {horo_text_list[i][1]}",
                description="",
                emoji=horo_emoji[horo_text_list[i][1]]
            ) for i in range(len(horo_text_list))
        ]
    )
    async def select_response(self, interaction: discord.Interaction, select: discord.ui.Select):
        i = int(select.values[0][0]) - 1
        embed = discord.Embed(
            title=f"{horo_text_list[i][0]}위 {horo_text_list[i][1]}",
            color=discord.Color.gold(),
            timestamp=datetime.now(timezone('Asia/Seoul')),
        )
        embed.add_field(name="",
                        value=f"{horo_text_list[i][2]}\n🍀 {horo_text_list[i][3]}",
                        inline=False)

        embed.set_author(name="오하아사 봇")
        embed.set_thumbnail(url=horo_thubnails[horo_text_list[i][1]])

        await interaction.response.send_message(embed=embed, ephemeral=True)

# 오하아사 메시지 보내는 함수
# 표시해둔 줄은 특정 시간에 메시지를 보내는 함수이니 코드 테스트 시 수정할 것
@tasks.loop(minutes = 2)
async def ohaasa_message():
    now = datetime.now(timezone('Asia/Seoul'))
    #if now.hour==7 and now.minute<=15: ### 테스트 시 조건 True로 수정
    if True:
      os.system("python3 crawllingOhaasa.py")

      channel = client.get_channel(CHANNEL_ID)

      embed = discord.Embed(
          title=datetime.strftime(now, '%Y년 %m월 %d일 오하아사 순위'),
          color=discord.Color.gold(),
          timestamp=datetime.now(timezone('Asia/Seoul')),
          url='https://www.asahi.co.jp/ohaasa/week/horoscope/'
      )
      for i in range(len(horo_text_list)):
          embed.add_field(name=f"{horo_text_list[i][0]}위- {horo_text_list[i][1]}",
                          value="",
                          inline=False)

      embed.set_author(name="오하아사 봇")
      embed.set_thumbnail(url='https://www.asahi.co.jp/ohaasa/week/horoscope/img/ttl_horoscope.png')

      await channel.send(embed=embed, view=SelectView())

# main과 비슷한 역할하는 부분
@client.event
async def on_ready():
    ohaasa_message.start()

    print("Hi, logged in as")
    print(client.user.name)
    print()

client.run(TOKEN)
