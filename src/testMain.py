import env
from discord.ext import commands

TOKEN = env.token
testingServers = env.serverList


# The basic bot instance in a separate file should look something like this:
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))
bot.load_extension("bingoButtons")
bot.load_extension("weeklyButtons")
bot.run(TOKEN)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}.")

print("Its running")