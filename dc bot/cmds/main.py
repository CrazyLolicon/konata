import discord
import random
import json
from discord.ext import commands
from core.core import Cog_Extension

with open('setting.json','r',encoding='utf8') as jfile:
     jdata = json.load(jfile)


class Main(Cog_Extension):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def pick(self,ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

def setup(bot):
    bot.add_cog(Main(bot))