from flask import Flask
from flask import render_template
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return render_template('index.html')

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()

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