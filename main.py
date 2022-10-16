import asyncio
import nextcord
import os

from discord_together import DiscordTogether
from keep_alive import keep_alive
from nextcord.ext import commands
from nextcord.ext import tasks

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = os.environ['TOKEN']
cogs = [
  'cogs.willkommen',
  'cogs.verify',
  'cogs.w2g',
  'cogs.regeln',
  'cogs.ping'
]
bot.remove_command(help)

@bot.event
async def on_ready():
  os.system('clear')
  print("----------------------------------")
  print("Loading cogs . . .")
  for cog in cogs:
    try:
      bot.load_extension(cog)
      print(cog + " was loaded.")
    except Exception as e:
      print(e)
  print("----------------------------------")
  print("Loading tasks . . .")
  bot.loop.create_task(status_task())
  print("status_task was loaded.")
  bot.loop.create_task(fahrer())
  print("fahrer was loaded.")
  bot.loop.create_task(team())
  print("team was loaded.")
  bot.loop.create_task(event_team())
  print("event_team was loaded.")
  bot.loop.create_task(bots())
  print("bots was loaded.")
  bot.loop.create_task(besucher())
  print("besucher was loaded.")
  bot.togetherControl = await DiscordTogether(TOKEN)
  print("----------------------------------")
  print("Nextcord verison:")
  print(nextcord.__version__)
  print("----------------------------------")
  print("Bot wurde gestartet.")
  print("Eingelogt als:")
  print(bot.user.name)
  print("Bot ID:")
  print(bot.user.id)
  print("----------------------------------")  

@bot.event
async def status_task():
  while True:
    await bot.change_presence(activity=nextcord.Streaming(name="Liveria VTC", url="https://www.twitch.tv/liveria_vtc/"), status=nextcord.Status.online)
    await asyncio.sleep(120)
    await bot.change_presence(activity=nextcord.Streaming(name="Die Starße ist alles", url="https://www.twitch.tv/liveria_vtc/"), status=nextcord.Status.online)
    await asyncio.sleep(120)

@tasks.loop(minutes=10)
async def fahrer():
  guild = bot.get_guild(1006895132018221196)
  kanal = bot.get_channel(1006895132076949573)
  role = guild.get_role(1006895132034990095)
  await kanal.edit(name=f"Fahrer - {len(role.members) + 1}")

@tasks.loop(minutes=10)
async def team():
  guild = bot.get_guild(1006895132018221196)
  kanal = bot.get_channel(1006895132076949574)
  role = guild.get_role(1006895132034990097)
  await kanal.edit(name=f"Team - {len(role.members)}")

@tasks.loop(minutes=10)
async def event_team():
  guild = bot.get_guild(1006895132018221196)
  kanal = bot.get_channel(1006895132336984084)
  role = guild.get_role(1006895132047585334)
  await kanal.edit(name=f"Event Team - {len(role.members)}")

@tasks.loop(minutes=10)
async def bots():
  guild = bot.get_guild(1006895132018221196)
  kanal = bot.get_channel(1006895132336984085)
  role = guild.get_role(1006895132034990090)
  await kanal.edit(name=f"Bots - {len(role.members)}")

@tasks.loop(minutes=10)
async def besucher():
  guild = bot.get_guild(1006895132018221196)
  kanal = bot.get_channel(1006895132336984086)
  role = guild.get_role(1006895132034990091)
  await kanal.edit(name=f"Besucher - {len(role.members)}")

keep_alive()
bot.run(TOKEN)