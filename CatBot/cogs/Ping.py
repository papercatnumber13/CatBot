import discord
from discord.ext import commands

client = discord.Client()

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #don't forget ()
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong (I hate decimals)')


def setup(bot):
    bot.add_cog(Ping(bot))
    print('Ping.py Setup Complete')

