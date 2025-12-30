import os
import discord

from src.bot import Client
from dotenv import load_dotenv

load_dotenv()

#

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(os.getenv("TOKEN"))
