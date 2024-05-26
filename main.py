import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Prevent the bot from replying to itself
    
    print(message)

    if not message.content == 'ping':
        await message.channel.send(message.content)

    await bot.process_commands(message)

bot.run(TOKEN)
