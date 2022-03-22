import discord
from discord.ext import commands

client = discord.Client()

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('bot is online, and running!')

@bot.command()
async def test(ctx):
    await ctx.reply('online!')

@bot.command()
async def add(ctx, num1:int, num2:int):
    await ctx.reply(num1+num2)

bot.run('token')
