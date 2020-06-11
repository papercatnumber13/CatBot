import discord
import random
from discord.ext import commands

client = discord.Client()


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def RNG(self, ctx, min, max):
        answer = random.randint(int(min), int(max))
        await ctx.send(answer)

    @commands.command()
    async def CoinFlip(self,ctx):
        answer = random.randint(1,2)
        if answer == 1:
            answer = 'Heads'
        else:
            answer = 'Tails'
        await ctx.send(answer)
        
    @commands.command()
    async def SafetyCheck(self,ctx):
        answer = random.randint(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
        if answer == 1:
            answer = 'Look Around You'
        else:
            answer = 'Safe'
        await ctx.send(answer)

def setup(bot):
    bot.add_cog(Random(bot))
    print('Random.py Setup Complete')
