import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def tutor(ctx):
    await ctx.send(f'Just tell me! $check_bottle, $check_paper, and $check_plastic')

@bot.command()
async def check_bottle(ctx):
    await ctx.send(f'It can decompose up to 450 years!')

@bot.command()
async def check_paper(ctx):
    await ctx.send(f'It can decompose for 4 weeks!')

@bot.command()
async def check_plastic(ctx):
    await ctx.send(f'It can decompose up to a millenium!')

bot.run("MTQ2Mzg4MjA4NDkyMDg1Njc5MQ.Ggn6ra.5xK9XJ-gWuhYCZM8vEwVlL1H7Snqff2cyp4Y8Q")
