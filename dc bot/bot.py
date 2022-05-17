import discord
from discord import channel
from discord import file
from discord.ext import commands
from discord.flags import Intents
import json
import random
import os


with open('setting.json', mode='r',encoding='utf8') as jfile:
     jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[',intents = intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['member']))
    await channel.send(f'{member}已登入戰場!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['member']))
    await channel.send(f'{member}已離開前線!')

@bot.event
async def on_massage(msg):
    keyword = ["Hi","hi","HI"]
    if msg.content in keyword:
        await msg.channel.send('hi hi')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} 完了.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'UN-Loaded {extension} 完了.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'RE-Loaded {extension} 完了.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
 bot.run(jdata['TOKEN'])