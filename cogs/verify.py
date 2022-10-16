import nextcord

from nextcord.ext import commands

class verify(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command
  @commands.dm_only()
  async def Rindfleisch(self, ctx, message):
    if messgae.author.bot:
      return
    else:
     guild = self.bot.get_guild(1006895132018221196)
    role = guild.get_role(1006895132034990091)
    embed=nextcord.Embed(title="Erfolg", color="0x7cfc98")
    embed.add_field(name="Du hast dich verifyzirt", value="Begrüße doch nett die anderen :D")
    await message.author.add_roles(role)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(verify(bot))