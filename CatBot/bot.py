import discord
import os
from discord.utils import get
from discord.ext import commands

client = commands.Bot(command_prefix = "+", case_insensitive=True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online,activity=discord.Game('Banning people for fun'))

extensions = ['cogs.Ping','cogs.Random','cogs.GuildNotif']

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)
        print(f'{extension} Loaded')

client.run('Njg5NTAwMDQwMTY2ODk5ODE5.Xtx4fA.W_8gesFfPDqoUxsbQpwgvAYeQjA')
