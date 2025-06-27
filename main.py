import asyncio
import discord
from discord.ext import commands, tasks
import datetime
from discord import FFmpegPCMAudio
#Traceback (most recent call last):
import pytz
from dotenv import load_dotenv
import os

jst = pytz.timezone('Asia/Tokyo')
load_dotenv()

current_time = datetime.datetime.now(jst)

print(current_time)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.event
async def on_ready():
    print("ログインしました!")
    await bot.change_presence(activity=discord.Game(name="音声"))

# ボイスチャンネルに参加して音声を再生する関数
async def play_voice(channel, audio_file):
    vc = await channel.connect()
    vc.play(FFmpegPCMAudio(audio_file))
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()

@tasks.loop(minutes=1)  # 1分ごとに実行
async def minutely_task():
    jst = pytz.timezone('Asia/Tokyo')

    current_time = datetime.datetime.now(jst)
    
    # 指定された時間帯
    target_times = [
    "00:00", "00:10", "00:20", "00:30", "00:40", "00:50",
    "01:00", "01:10", "01:20", "01:30", "01:40", "01:50",
    "02:00", "02:10", "02:20", "02:30", "02:40", "02:50",
    "03:00", "03:10", "03:20", "03:30", "03:40", "03:50",
    "04:00", "04:10", "04:20", "04:30", "04:40", "04:50",
    "05:00", "05:10", "05:20", "05:30", "05:40", "05:50",
    "06:00", "06:10", "06:20", "06:30", "06:40", "06:50",
    "07:00", "07:10", "07:20", "07:30", "07:40", "07:50",
    "08:00", "08:10", "08:20", "08:30", "08:40", "08:50",
    "09:00", "09:10", "09:20", "09:30", "09:40", "09:50",
    "10:00", "10:10", "10:20", "10:30", "10:40", "10:50",
    "11:00", "11:10", "11:20", "11:30", "11:40", "11:50",
    "12:00", "12:10", "12:20", "12:30", "12:40", "12:50",
    "13:00", "13:10", "13:20", "13:30", "13:40", "13:50",
    "14:00", "14:10", "14:20", "14:30", "14:40", "14:50",
    "15:00", "15:10", "15:20", "15:30", "15:40", "15:50",
    "16:00", "16:10", "16:20", "16:30", "16:40", "16:50",
    "17:00", "17:10", "17:20", "17:30", "17:40", "17:50",
    "18:00", "18:10", "18:20", "18:30", "18:40", "18:50",
    "19:00", "19:10", "19:20", "19:30", "19:40", "19:50",
    "20:00", "20:10", "20:20", "20:30", "20:40", "20:50",
    "21:00", "21:10", "21:20", "21:30", "21:40", "21:50",
    "22:00", "22:10", "22:20", "22:30", "22:40", "22:50",
    "23:00", "23:10", "23:20", "23:30", "23:40", "23:50"
    ]


    current_time_str = current_time.strftime("%H:%M")  # 現在の時間を"HH:MM"形式の文字列に変換
    print(current_time_str)

    if current_time_str in target_times:
        # ボイスチャンネルに参加して音声を再生
        CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID"))
        voice_channel = bot.get_channel(CHANNEL_ID)
        
        if voice_channel:
            await play_voice(voice_channel, "jihoutest.mp3") 

@minutely_task.before_loop
async def before_minutely_task():
    await bot.wait_until_ready()

minutely_task.start()

# @tasks.loop(hours=1)  # 1時間ごとに実行
# async def hourly_task():
#     current_time = datetime.datetime.now().time()
    
#     # ここで特定の時間帯を指定
#     target_hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    
#     if current_time.hour in target_hours:
#         # ボイスチャンネルに参加して音声を再生
#        CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID"))
#        voice_channel = bot.get_channel(CHANNEL_ID)
#        if voice_channel:
#           await play_voice(voice_channel, "jihoutest.mp3")

# @hourly_task.before_loop
# async def before_hourly_task():
#     await bot.wait_until_ready()

# hourly_task.start()

@bot.command()
async def ping(ctx):
    raw_ping = bot.latency
    ping = round(raw_ping * 1000)
    await ctx.reply(f"Pong\nBotのPing値は{ping}msです。")

@bot.command()
async def test(ctx):
    await ctx.send("test")


TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)