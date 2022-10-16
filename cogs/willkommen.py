import nextcord
import random

from nextcord.ext import commands

class willkommen(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    if not member.bot:
      gifs = [
        'https://share.creavite.co/GfBmufNARKSs9DM0.gif',
				'https://share.creavite.co/DmgqQrUdPdtoqc4h.gif',
				'https://share.creavite.co/cNog0Jd4s1OgsE4e.gif'
      ]
      channel_willkommen = self.bot.get_channel()
      guild = member.guild
      RegelwerkC = guild.egt_channel()
      embed = nextcord.Embed(
        title=f'Willkommen zum {member.guild.name}',
        description=f'Willkommen {member.mention}.',
        color=nextcord.random
      )
      embed.add_field(name='Lies die Regeln hier', value=f'{RegelwerkC.mention}', inline=False)
      embed.set_image(url=random.choice(gifs))
      embed.set_author(name='Liveria VTC', icon_url='https://ibb.co/dG6PWgC')
      await channel_willkommen.send(embed=embed)
    else:
      guild = self.bot.get_guild(1006895132018221196)
      role = guild.get_role(1006895132034990090)
      await member.add_roles(role)
      
def setup(bot):
  bot.add_cog(willkommen(bot))