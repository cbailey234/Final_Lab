# bot.py
import os
import random
from discord.ext import commands
from datetime import datetime
TOKEN = ('NzA2OTQ3NTQ0MTU2MDc4MDky.XrGbIw.1ml99yew9by1ajmM9hTWn1kcBaU')
GUILD = ('Zeusbot90')

bot = commands.Bot(command_prefix='!')

@bot.command(name='Zeus', help='Responds with the Mighty Zeus')
async def Zeus_God(ctx):
    Zeus_God_Quotes = [
        'LIGHTNING BOLT!!!',
        (
            'I AM THE MIGHTY ZEUS!!!' ),
        ]
    response = random.choice(Zeus_God_Quotes)
    await ctx.send(response)
@bot.command(name='date', help='Responds date and time')
async def date(ctx):
    now = datetime.now()
    date = now.strftime("%m/%d/%y, %H:%M:%S")
    response = date
    await ctx.send(response)


bot.run(TOKEN)

