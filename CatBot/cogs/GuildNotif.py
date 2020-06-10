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

def setup(bot):
    bot.add_cog(GuildNotif(bot))
    print('GuildNotif.py Setup Complete')
