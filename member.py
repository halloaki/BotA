import discord
from discord.ext import commands
import random


class Members():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball',
                      description="Might answer a yes/no question.",
                      brief="Answers a yes or no question.",
                      aliases=['eight_ball', 'eightball', '8-ball'],
                      pass_context=True)
    async def eight_ball(self, context):
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
        await self.bot.say(random.choice(possible_responses)+', ' + context.message.author.mention)

    @commands.command(name='roll',
                      description="rolls a dice (between 1 and 6)",
                      brief="rolls a dice",
                      aliases=['dice'],
                      pass_context=True)
    async def roll(self, context):
        possible_numbers = [
            ':one:',
            ':two:',
            ':three:',
            ':four:',
            ':five:',
            ':six:',
        ]
        await self.bot.client.say(context.message.author.mention + ' rolled a ' + random.choice(possible_numbers))

    @commands.command(name='cookie',
                      description='Gives a person a cookie',
                      brief='Gives a cookie', pass_context=True)
    async def cookie(self, context):
        content = context.message.content[12:]
        message = content.split(" ")
        if message[0] == "":
            await self.bot.say("You have to give the cookie to someone")
        elif message[0].lower() == "bota":
            await self.bot.say(":heart: Thank you :heart:")
        elif message[0].lower() in str(context.message.author).lower():
            await self.bot.say("You can't give a cookie to yourself!")
        else:
            await self.bot.say(context.message.author.mention + ' gave a cookie to ' + str(message))

    @commands.command(name='say',
                      description="The bot will say something in your place",
                      brief='bot says something', pass_context=True)
    async def say(self, context):
        await self.bot.say(context.message.content[8:])
        await self.bot.delete_message(context.message)

    @commands.command(name="water", description="The bot may give you some water, or not.",
                      brief='bot distributes water', pass_context=True)
    async def water(self, context):
        phrases = [
            ' The shaman made it rain, hopefully it isn\'t acid rain like last time',
            ' You manage to scavenge water in the back of Miraz home <:water:438082707688259584>',
            ' sorry we don\'t have water for everybody today...',
            ' sorry maybe the shaman will make it rain tomorrow...',
            ' The well has dried up!'
        ]
        await self.bot.say(context.message.author.mention + random.choice(phrases))

    @commands.command(name="roulette",
                      description="You load a revolver with 1 bullet in the 6 slots, you spin the roulette and hope you don't get the bullet",
                      brief="play the roulette", pass_context=True)
    async def roulette(self, context):
        randomNumber = random.randint(1, 6)
        message = ""
        possibleDeaths = [
            "💀Everyone looked with fear in their eyes as they could see " +
            str(context.message.author) + " brains over the wall.💀",
            str(context.message.author) +
            " head exploded like a ripe tomato, leaving a terrible mess for the others to clean.",
        ]
        possibleLives = [
            "While " + str(context.message.author) +
            " was peeing their pants in the fear of death, they heard a clicking noice. It seems that they were lucky this time...",
        ]
        if(randomNumber == 6):
            message = random.choice(possibleDeaths)
        else:
            message = random.choice(possibleLives)
        await self.bot.say(context.message.author.mention + " loaded the first bullet into the chamber and spinned it. they pointed the gun towards their head and pulled the trigger.\n \n" + message)


def setup(bot):
    bot.add_cog(Members(bot))
