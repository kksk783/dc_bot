import discord 
from discord.ext import commands

intents=discord.Intents.all()
bot = commands.Bot(command_prefix="",intents=intents)

@bot.event
async def on_ready():
    print(f">>Bot ({bot.user}) is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1378733818927906827)
    await channel.send(f"{member} 加入了!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1378728174351028234)
    await channel.send(f"{member} 離開了!")


bot.run("tk") 