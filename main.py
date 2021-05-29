# Prerequisite:
# Make a file called '.env'
# In that file, type 'token = <your bot token>'

import discord
from discord.ext import commands
import os
import dotenv

# Set this to the prefix you want for your bot.
prefix = ">"
client = commands.Bot(command_prefix=prefix)

# Removing the defualt help command so we can use our custom help command
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot online!")

# You can do the following if you're using replit.com and this
# method dosen't work:
# client.run(os.getenv('token'))
dotenv.load_dotenv()
client.run(os.environ.get("token"))
