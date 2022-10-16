import nextcord

from nextcord.ext import commands

class w2g(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def w2g(self, ctx, message):
    link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    embed=nextcord.Embed(title="Erfolgreich", color='0x7cfc98')
    embed.add_field(name="Drücke den Link", value=f"{link}")
    await ctx.send(embed=embed)
    await message.delete()

def setup(bot):
  bot.add_cog(w2g(bot))