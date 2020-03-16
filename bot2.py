import os
import discord
from discord.ext import commands
client = commands.Bot(command_prefix ="/")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle , activity=discord.Game("helping people . "))
	print("ok")
@client.event
async def on_message(message):
	Nmessage = message.content
	if message.author.id==687395558477791245:
		print("ho")
	else:
	
		if str(message.channel.type) == "private":
			Nmessage = message.content
			channel = client.get_channel(688788263321993277)
			embed=discord.Embed(title="Confession .",color=0x00ff00, description="A new confession  .")
			embed.add_field(name="Confession :", value=Nmessage, inline=False)
			await channel.send(embed=embed)
	await client.process_commands(message)
@client.command()
async def helps(ctx,*,prob):
	author = ctx.message.author
	user = client.get_user(475818993568055298)
	await user.send(f"{author} have a problem :   {prob}")
        await ctx.send("your message is sent ")

client.run(os.getenv('Token'))
