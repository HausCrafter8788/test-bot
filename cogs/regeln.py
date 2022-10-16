import asyncio
import nextcord
from nextcord.ext import commands


class regeln(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def regeln(self, ctx):
    if ctx.message.author.id == (950746398524047370):
      embed = nextcord.Embed(name="Regeln", color=nextcord.Color.green())
      embed.add_field(
        name='1.',
        value='Die Regeln sind zu befolgen (Unwissenheit schützt vor strafe nicht)',
        inline=False)
      embed.add_field(
        name='2.',
        value='Bei einem convoi entscheidet der höste rang die anordnung',
        inline=False)
      embed.add_field(
        name='3.',
        value='Es wird stets ein guter Umgang gefordert (mal als spaß zu Beleidigen ist ok es solte aber auch so zu verstehen zu sein',
        inline=False)
      embed.add_field(
        name='4.',
        value='Rassistische, sexistische, rechts- bzw. linksextremistische und nicht jugendfreie (pornografische) Nicknames sind verboten.',
        inline=False)
      embed.add_field(
        name='5.',
        value='Spamming, sowie Links posten ist zu unterlassen.',
        inline=False)
      embed.add_field(
        name='6.',
        value='Caps sowie Zalgos sind untersagt.',
        inline=False)
      embed.add_field(
        name='7.',
        value='Das Ausführen von gewerblichen Aktivitäten (z. B. der Handel mit Accounts oder Echtgeld) ist untersagt.',
        inline=False)
      embed.add_field(
        name='8.',
        value='Das Betteln nach Rängen ist untersagt.',
        inline=False)
      embed.add_field(
        name='9.',
        value='Das secret wort ist Rindfleisch send dies dem bot der die nachricht gesendet hat',
        inline=False)
      embed.add_field(
        name='10.',
        value='Keine NSFW- oder obszönen Inhalte. Dazu zählen Texte, Bilder oder Links mit Nacktheit, Sex, schwerer Gewalt oder anderen grafisch verstörenden Inhalten.',
        inline=False)
      embed.add_field(
        name='11.',
        value='Der öffentliche Chat sollte von privaten Diskussionen frei gehalten werden.',
        inline=False)
      embed.add_field(
        name='12.',
        value='Störgeräusche werden mit einer Aufforderung zum muten oder mit einem temporären Voice Chat Mute bestraft.',
        inline=False)
      embed.add_field(
        name='13.',
        value='Skripte/Spoiler sind zu unterlassen, falls diese keine/n Skript/Spoiler darstellen. ||Das ist ein Spoiler|| ```Das ist ein Skript```',
        inline=False)
      embed.add_field(
        name='14.',
        value='*Fett*, **Kursiv** und __Unterstrichen__ ist nur spärlich zu verwenden.',
        inline=False)
      embed.add_field(
        name='15.',
        value='Das umgehen einer aktiven Strafe durch einen 2. Account wird mit einem permanenten Serverausschluss geahndet.',
        inline=False)
      embed.add_field(
        name='16.',
        value='Private Daten, wie Telefonnummer, Adresse, Bilder, etc. solltest du nie veröffentlichen. Ein Teammitglied wird dich niemals nach diesen Daten oder Passwörtern fragen. (auser bei der Bewerbung)',
        inline=False)
      embed.add_field(
        name='17.',
        value='Teammitglieder behalten sich das Recht vor, eine Sanktion gegen einen Spieler auszusprechen, dessen Betragen nicht mit den allgemeinen Normen des Verhaltens übereinstimmt, auch, wenn bis dahin der konkrete Regelbruch nicht im Regelwerk genannt ist.',
        inline=False)
      embed.add_field(
        name='18.',
        value='Anweisungen der Teammitglieder ist Folge zu leisten.',
        inline=False)
      embed.add_field(
        name='19.',
        value='Das Serverteam hat das Hausrecht und kann mit Angaben von Gründen jederzeit davon Gebrauch machen.',
        inline=False)
      await ctx.send(embed=embed)
      await asyncio.sleep(5)
      embed = nextcord.Embed(
        title="Finde das Secret Wort",
        description='Es ist irgendwo in den Regeln Versteckt :D viel spaß beim lesen',
        color=nextcord.Color.random())
      
      await ctx.send(embed=embed)
    else:
      return


def setup(bot):
    bot.add_cog(regeln(bot))