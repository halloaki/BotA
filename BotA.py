from discord.ext.commands import Bot
import random
import const

# Constants
BOT_PREFIX = const.BOT_PREFIX
TOKEN = const.TOKEN
client = Bot(command_prefix=BOT_PREFIX)
startup_extensions = ["member"]

# Commands

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Load in the extensions?
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
# Activates the bot

client.run(TOKEN)
