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

    embed.set_author(
        name=f'User Banned | {member}', icon_url=member.avatar_url)

    embed.add_field(name='User', value=f'{member.mention}', inline=True)

    embed.add_field(name='Moderator',
                    value=f'{ctx.author.mention}', inline=True)

    embed.add_field(name='Reason', value=f'{reason}', inline=True)

    # Embed which will be DMed to the person who was banned
    embed2 = discord.Embed(
        description=f'You were banned from {ctx.guild.name}', colour=0xFF0000)

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


'''
You can do the following if you're using replit.com and this
method dosen't work:
client.run(os.getenv('token'))
You can also use the following if no one can see your code:
client.run(<your bot token here>)
This way you don't need a '.env' file and no need to import os and dotenv
Keep in mind that if someone can see your code, they will we able to see 
your bot token and get access to your bot.
'''

dotenv.load_dotenv()
client.run(os.environ.get("token"))
