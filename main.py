import discord
import os
import requests
import shutil

from discord.ext import commands

token = "replace me with your discord token" # <<<<<

client = commands.Bot(command_prefix=".", self_bot=True)

@client.event
async def on_ready():
	print("Ready")

@client.command()
async def save(ctx, channel:discord.TextChannel=None):
	if channel == None:
		ctx.message.channel

	await ctx.message.delete()
	async for message in channel.history():
		if message.attachments != None:
			for attachment in message.attachments:
				file = requests.get(attachment.url, stream=True)
				try:
					open(f'{channel.name}/{attachment.filename}', 'wb').write(file.content)

				except:
					os.makedirs(channel.name)
					open(f'{channel.name}/{attachment.filename}', 'wb').write(file.content)

				print(f"Saved {attachment.filename}")

	shutil.make_archive(channel.name, 'zip', channel.name)

client.run(token, bot=False)