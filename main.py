import discord
from discord.ext import commands
from dotenv import load_dotenv
from loguru import logger
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user} (ID: {bot.user.id})')


@bot.event
async def on_connect():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_command_error(ctx, error):
    logger.info(f'CALLED on_command_error with {error}')

    if isinstance(error, commands.CommandNotFound):
        # Handle CommandNotFound error here
        await ctx.send("Sorry, that command doesn't exist.")
    else:
        # Log other errors
        logger.error(f'An error occurred: {error}')

bot.run(TOKEN)
