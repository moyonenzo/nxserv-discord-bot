import os
import discord

try:
    from src.bot import Client
except ModuleNotFoundError:
    from bot import Client

from dotenv import load_dotenv

load_dotenv()

#

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(os.getenv("TOKEN"))
