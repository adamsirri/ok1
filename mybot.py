
from discord.ext.commands import has_permissions,CheckFailure
import discord
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
	vodka= client.get_user(475818993568055298)
	shy=client.get_user(340542114477768705)
	cram=client.get_user(212241077695021056)
	theo=client.get_user(524704812432883722)
	aki=client.get_user(416667474004803584)
	await aki.send(f"{author} have a problem :   {prob}")
	await vodka.send(f"{author} have a problem :   {prob}")
	await cram.send(f"{author} have a problem :   {prob}")
	await theo.send(f"{author} have a problem :   {prob}")
	await shy.send(f"{author} have a problem :   {prob}")
	
	
	await ctx.send("your message is sent ")
@client.command()
async def punch(ctx,member:discord.Member):
	au = ctx.message.author
	embed1=discord.Embed(title=f"{au} punched {member}")
	embed1.set_thumbnail(url="https://i.pinimg.com/originals/8d/50/60/8d50607e59db86b5afcc21304194ba57.gif")
	channel1 = client.get_channel(683350752747585554)
	await channel1.send(embed=embed1)
@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def Cban(ctx,member:discord.Member,*,reason=None):
	await member.ban(reason=reason)
	embed=discord.Embed(title=f"{member} get banned ... I feel so powerful muahaha . Signed Confession")
	embed.set_thumbnail(url="https://thumbs.gfycat.com/CheapPhonyBeardeddragon-small.gif")
	channel2 = client.get_channel(683350466154856454)
	await channel2.send(embed=embed)
	
@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def Ckick(ctx,member:discord.Member,*,reason=None):
	
	await member.kick(reason=reason)	
	embed=discord.Embed(title=f"{Member} got kicked .... it's not me i am just a bit.")
	embed.set_thumbnail(url="https://media.tenor.com/images/67f1ef894af69f5d2a99501b0ef3f686/tenor.gif")
	channel2 = client.get_channel(683350466154856454)
	await channel2.send(embed=embed)

@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def DeleteThatShit(ctx,*,ammount=5):
	await ctx.channel.purge(limit=ammount)
client.run(os.getenv('Token'))
