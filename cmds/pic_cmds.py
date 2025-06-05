import discord 
from discord.ext import commands

class pic_cmds(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.tree.command(name="一個一個",description="快端上來罷!")
    async def stinky_command(interaction: discord.Interaction):
         await interaction.response.send_message("你是一個一個一個\n",file=discord.File(jdata["pic"][1]))

    @commands.tree.command(name="一輩子",description="要組一輩子樂團")
    async def forever(interaction: discord.Interaction):
        await interaction.response.send_message(file=discord.File(jdata["pic"][0]))

def setup(bot):
    bot.add_cog(pic_cmds(bot))