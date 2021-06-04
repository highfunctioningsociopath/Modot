'''
Prerequisite:
Make a file called '.env'
In that file, type 'token = <your bot token>'
'''

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


# Kick command
@client.command(name="kick", aliases=["Kick", "KICK"])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    # Embed which will be sent when a person is kicked
    embed = discord.Embed(colour=0xFF0000)

    embed.set_author(name=f'User Kicked | {member}', icon_url=member.avatar_url)

    embed.add_field(name='User', value=f'{member.mention}', inline=True)

    embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)

    embed.add_field(name='Reason', value=f'{reason}', inline=True)
    
    # Embed which will be DMed to the person who was kicked
    embed2 = discord.Embed(description=f'You were kicked from {ctx.guild.name}', colour=0xFF0000)
    
    embed2.add_field(name='Reason', value=f'{reason}', inline=True)
    
    embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)
    
    
    await ctx.send(embed=embed)  # Sends an embed with info in the 
                                 # channel the command was used on
    await member.send(embed=embed2)  # DMs an embed with kick info
                                     # to the person who was kicked
    await member.kick(reason=reason)
    

# Ban command
@client.command(name="ban", aliases=["Ban", "BAN"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    # Embed which will be sent when a person is banned
    embed = discord.Embed(colour=0xFF0000)

    embed.set_author(name=f'User Banned | {member}', icon_url=member.avatar_url)

    embed.add_field(name='User', value=f'{member.mention}', inline=True)

    embed.add_field(name='Moderator', value=f'{ctx.author.mention}', inline=True)

    embed.add_field(name='Reason', value=f'{reason}', inline=True)

    # Embed which will be DMed to the person who was banned
    embed2 = discord.Embed(description=f'You were banned from {ctx.guild.name}', colour=0xFF0000)

    embed2.add_field(name='Reason', value=f'{reason}', inline=True)

    embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

    await ctx.send(embed=embed)  # Sends an embed with info in the
                                 # channel the command was used on
    await member.send(embed=embed2)  # DMs an embed with ban info
                                     # to the person who was banned
    await member.ban(reason=reason)


# Softban command
@client.command(name="softban", aliases=["Softban", "SOFTBAN"])
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member, *, reason=None):
    # Embed which will be sent when a person is softbanned
    embed = discord.Embed(colour=0xFF0000)

    embed.set_author(name=f'User Softanned | {member}', icon_url=member.avatar_url)

    embed.add_field(name='User', value=f'{member.mention}', inline=True)

    embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)

    embed.add_field(name='Reason', value=f'{reason}', inline=True)

    # Embed which will be DMed to the person who was softbanned
    embed2 = discord.Embed(description=f'You were softbanned from {ctx.guild.name}', colour=0xFF0000)

    embed2.add_field(name='Reason', value=f'{reason}', inline=True)

    embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

    await ctx.send(embed=embed)  # Sends an embed with info in the
                                 # channel the command was used on
    await member.send(embed=embed2)  # DMs an embed with softban 
                                     # info to the person who was softbanned
    await member.ban(reason=reason)
    await member.unban(reason=reason)


# Help command
@client.command(name="help", aliases=["Help", "HELP"])
async def help(ctx):
    # Embed with list of all commands
    embed = discord.Embed(description="List of all commands:", colour=0x000000)
    
    embed.add_field(name="help", value="Shows a list of all commands.", inline=True)
    
    embed.add_field(name="warn", value="Warns the specified user.", inline=True)
    
    embed.add_field(name="warnings", value="Shows all the warnings of the specified user.", inline=True)
    
    embed.add_field(name="mute", value="Mutes the specified user.", inline=True)
    
    embed.add_field(name="kick", value="Kicks the specified user.", inline=True)
    
    embed.add_field(name="softban", value="Softbans the specified user.", inline=True)
    
    embed.add_field(name="ban", value="Bans the specified user.", inline=True)
    
    await ctx.send(embed=embed)


# Mute command
@client.command(name="mute", aliases=["Mute", "MUTE"])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    muteRole = discord.utils.get(ctx.guild.roles, name="mute")
    
    if not muteRole:
        muteRole = await ctx.guild.create_role(name="Muted")
        
        for channel in ctx.guild.channels:
            await channel.set_permissions(muteRole, speak=False, send_messages=True)
    
    # Embed which will be sent when a person is muted
    embed = discord.Embed(colour=0xFF0000)

    embed.set_author(name=f'User Muted | {member}', icon_url=member.avatar_url)

    embed.add_field(name='User', value=f'{member.mention}', inline=True)

    embed.add_field(name='Moderator', value=f'{ctx.author.mention}', inline=True)

    embed.add_field(name='Reason', value=f'{reason}', inline=True)

    # Embed which will be DMed to the person who was muted
    embed2 = discord.Embed(description=f'You were banned in {ctx.guild.name}', colour=0xFF0000)

    embed2.add_field(name='Reason', value=f'{reason}', inline=True)

    embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)
    
    await member.add_roles(muteRole, reason=reason)
    await ctx.send(embed=embed)  # Sends an embed with info in the
                                 # channel the command was used on
    await member.send(embed=embed2)  # DMs an embed with mute
                                     # info to the person who was mute

# Gets the environment variable "token" you made in .env file(read line 2-4 if you havn't done it)
dotenv.load_dotenv()
client.run(os.environ.get("token"))
