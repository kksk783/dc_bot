import discord 
from discord.ext import commands

intents=discord.Intents.all()

bot = commands.Bot(command_prefix="",intents=intents)

@bot.event
async def on_ready():
    print(f">>Bot ({bot.user}) is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel()

@bot.event
async def on_member_remove(member):
    print(f"{member} leave!")


bot.run("token")



