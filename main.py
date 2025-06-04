import discord 
from discord.ext import commands
import json

with open("setting.json",mode='r',encoding='utf8') as jFile:
    jdata=json.load(jFile)
    print(f"fdata:{jdata}")


intents=discord.Intents.all()
bot = commands.Bot(command_prefix="",intents=intents)

@bot.event
async def on_ready():
    # slash = async.
    print(f">>Bot ({bot.user}) is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(jdata["welcome_Channel"])
    if channel:
        await channel.send(f"{member} 加入了!")
    else:
        print(f"not found welcome:{int(jdata['welcome_Channel'])} ")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(jdata["leave_Channel"])
    if channel:
        await channel.send(f"{member} 離開了!")
    else:
        print(f"not found leave:{int(jdata['leave_Channel'])}")


@bot.command()
async def ping(ctx):
    await ctx.send(f"機器人延遲:{round(bot.latency*1000)}(ms)")


bot.run(jdata["TOKEN"]) 