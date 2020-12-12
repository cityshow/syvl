import discord
import sys

from discord.ext import commands
from config.py import *

if str(sys.argv[1]) == "log-all":
	print("All Message Logging Set To True.")
else:
	print("All Message Logging Set To False.")

client = commands.Bot(command_prefix = "syvl: ", self_bot = True)

@client.event
async def on_ready():
	print(f"Welcome To Syvl, {client.user}.")
	print("Prefix: syvl:\n")

@client.listen("on_message_delete")
async def log(message):
	try:
		print(f"Message deleted in guild {message.guild}, Message Contents Being \"{message.content}\".\nGuild ID being {message.guild.id}.\nMessage From User {message.author}, Message author ID being {message.author.id}.\n\n")
	except:
		print("Please Use The Bot In Servers Only. Direct Message Support Will Come Later.\n\n")

client.listen("on_message")
async def all_log(message):
	if str(sys.argv[1]).lower() == "log-all":
		print(f"Message Sent in guild {message.guild}, Guild ID being {message.guild.id}.\nMessage From User {message.author}, Message author ID being {message.author.id}.\nMessage Sent At {datetime.now}.\n\n")

@commands.command()
async def exit(ctx):
	await ctx.message.delete()
	print(f"Bye, {client.user}.")
	sys.exit()

client.run(token, bot = False)

# To Do:
# Add Channel ID
# Add Channel Name Msg Sent In
