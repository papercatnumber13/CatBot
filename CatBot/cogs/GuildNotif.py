import discord
from discord.ext import commands

class GuildNotif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}!'.format(member))
            
    @commands.command()
    async def SafetyCheck(self,ctx):
        answer = random.randint(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
        if answer == 1:
            answer = 'DANGER'
        else:
            answer = 'Safe'
        await ctx.send(answer)
    

def setup(bot):
    bot.add_cog(GuildNotif(bot))
    print('GuildNotif.py Setup Complete')
