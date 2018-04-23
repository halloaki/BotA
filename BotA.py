from discord.ext.commands import Bot
import random

# Constants
BOT_PREFIX = "bota "
TOKEN = "NDI2ODU5ODE1MDM4NDg0NDkx.Db-xUg.TpMfUJucYXucACa3cai_h779ZJc"
client = Bot(command_prefix=BOT_PREFIX)

# Commands


@client.command(name='8ball',
                description="Might answer a yes/no question.",
                brief="Answers a yes or no question.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Doesn\'t look like it',
        'Probably not',
        'I can only see so far in the future',
        'It is likely',
        'Perhaps',
        'If I say yes, will you leave me alone?',
        'Yes, no, maybe...',
        'Do I look like a magical ball that tells the future? Oh wait...',
        'Yes',
        'No',
    ]
    await client.say(random.choice(possible_responses)+', ' + context.message.author.mention)


@client.command(name='roll',
                description="rolls a dice (between 1 and 6)",
                brief="rolls a dice",
                aliases=['dice'],
                pass_context=True)
async def roll(context):
    possible_numbers = [
        ':one:',
        ':two:',
        ':three:',
        ':four:',
        ':five:',
        ':six:',
    ]
    await client.say(context.message.author.mention + ' rolled a ' + random.choice(possible_numbers))


@client.command(name='cookie',
                description='Gives a person a cookie',
                brief='Gives a cookie', pass_context=True)
async def cookie(context, message: str):
    await client.say(context.message.author.mention + ' gave a cookie to ' + str(message))


@client.command(name='say',
                description="The bot will say something in your place",
                brief='bot says something', pass_context=True)
async def say(context, message: str):
     await client.say(context.message.content[8:])
     await client.delete_message(context.message)

# Activates the bot

client.run(TOKEN)
