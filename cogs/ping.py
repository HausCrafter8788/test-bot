import nextcord
from nextcord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        if round(self.bot.latency * 1000) <= 50:
            embed=nextcord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! Der ping ist **{round(self.bot.latency *1000)}** ms!", color=0x44ff44)
        elif round(self.bot.latency * 1000) <= 100:
            embed=nextcord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! Der ping ist **{round(self.bot.latency *1000)}** ms!", color=0xffd000)
        elif round(self.bot.latency * 1000) <= 200:
            embed=nextcord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! Der ping ist **{round(self.bot.latency *1000)}** ms!", color=0xff6600)
        else:
          embed=nextcord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! Der ping ist **{round(self.bot.latency *1000)}** ms!", color=0x990000)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ping(bot))