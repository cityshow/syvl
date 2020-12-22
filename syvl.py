import discord
import asyncio
import sys
from discord.ext import commands

try:
	if str(sys.argv[1]).lower() == "true":
		print("Edit Message Logging Set To True.")
	else:
		print("Edit Message Logging Set To False.")
except:
	print("Please use valid arguments.")
	arguments = "python3 Syvl.py (Option To Enable Edit Logging, true/false)"
	print(arguments); sys.exit()

client = commands.Bot(command_prefix = "Syvl: ", self_bot = True)
blacklist = [409107086526644234, 234395307759108106, 155149108183695360, 439205512425504771] # Just some bots
gblacklist = [645753561329696785, 267624335836053506]

@client.event
async def on_ready():
	print(f"Welcome To Syvl, {client.user}.")
	print("Prefix: Syvl:\n")

@client.listen("on_message_delete")
async def log(message):
	if message.content != "" and message.author.id not in blacklist and message.guild.id not in gblacklist:
		try:
			print("Message Deletion Detected")
			print(f"Message Deleted, Message Contents Being \"{message.content}\", message ID being {message.id}.")
			print(f"Message From User {message.author}, Message author ID being {message.author.id}.")
			print(f"Message Sent In Guild {message.guild}, Guild ID being {message.guild.id}.")
			print(f"Message Sent In Channel {message.channel}, Channel ID Being {message.channel.id}.")
			print(f"Message Sent At {message.created_at}.\n\n\n")
		except:
			print("Message Deletion Detected In Direct Messages.\n\n\n")
			print(f"Full Message Contents Being {message.content}, And Message ID Being {message.id}.")
			print(f"Message From User {message.author}, Message author ID being {message.author.id}.")
			print(f"Message Sent At {message.created_at}.\n\n\n")

@client.listen("on_message_edit")
async def editlog(before, after):
	if before.content != "" and after.content != "" and before.author.id not in blacklist and before.guild.id not in gblacklist and str(sys.argv[1]).lower() == "true":
		try:
			print("Message Edit Detected")
			print(f"Message Edited, Message Contents Being \"{before.content}\".")
			print(f"Message After Edit Being \"{after.content}\", and message ID being {before.id}.")
			print(f"Message From User {before.author}, Message Author ID Being {before.author.id}.")
			print(f"Message Sent In Guild {before.guild}, Guild ID being {before.guild.id}.")
			print(f"Message Sent In Channel {before.channel}, Channel ID Being {before.channel.id}.")
			print(f"Message Sent At {before.created_at}.\n\n\n")
		except:
			print("Message Edit Detected In Direct Messages.\n\n\n")
			print(f"Full Message Contents Being {message.content}, And Message ID Being {message.id}.")
			print(f"Message From User {message.author}, Message author ID being {message.author.id}.")
			print(f"Message Sent At {message.created_at}.\n\n\n")
@client.listen("on_message")
async def GarlicBread(message):
	if "garlic bread" in message.content.lower() and message.author != client.user:
		print("Garlic Bread Detected")
		try:
			print(f"Message From User {message.author}, Message author ID being {message.author.id}.")
			print(f"Full Message Contents Being {message.content}, and message ID being {message.id}.")
			print(f"Message Sent In Guild {message.guild}, Guild ID being {message.guild.id}.")
			print(f"Message Sent In Channel {message.channel}, Channel ID Being {message.channel.id}.")
			print(f"Message Sent At {message.created_at}.\n\n\n")
			await message.channel.send("Mmmmm, Garlic Bread")
			await asyncio.sleep(1)
		except:
			print("Garlic Bread Detected In Direct Messages.\n\n\n")
			print(f"Full Message Contents Being {message.content}, And Message ID Being {message.id}.")
			print(f"Message From User {message.author}, Message author ID being {message.author.id}.")
			print(f"Message Sent At {message.created_at}.\n\n\n")
			await message.channel.send("Mmmmm, Garlic Bread")
			await asyncio.sleep(1)

@commands.command()
async def exit(ctx):
	await ctx.message.delete()
	print(f"Bye, {client.user}.")
	sys.exit()
client.run(token, bot = False)
