import discord 
from discord.ext import commands
import json

with open("./mainBot/setting.json",mode='r',encoding='utf8') as jFile:
    jdata=json.load(jFile)
    
intents=discord.Intents.all()
bot = commands.Bot(command_prefix="",intents=intents)
# file = discord.File("C:/Users/a0981/Downloads/dc_bot-main/pic/forever.jpg")
# embed = discord.Embed(color=discord.Color.blue())

# embed.set_image(url="attachment://C:/Users/a0981/Downloads/dc_bot-main/pic/forever.jpg")


@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f">>Bot ({bot.user}) is online")
    print(f">>已同步 {len(slash)} 個 slash 指令")

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
        print(f"not found leave:{(jdata['leave_Channel'])}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"機器人延遲:{round(bot.latency*1000)}(ms)")

# @bot.event
# async def on_message(message):
#     if message.author.bot:
#         return
#     print(f"收到消息{message.content}了")
#     channel = bot.get_channel(message.channel.id)
#     if message.content=="114514":
#         await channel.send("いいよ！ こいよ！")



# @bot.tree.command(name="一輩子",description="要組一輩子樂團")
# async def stinky_command(interaction: discord.Interaction):
#     await interaction.response.send_message(file=file,embed = embed)



bot.run(jdata["TOKEN"]) 