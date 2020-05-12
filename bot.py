# bot.py

import re
import requests
import argparse
from bs4 import BeautifulSoup
import os
import random
from discord.ext import commands
from datetime import datetime
TOKEN = ('NzA2OTQ3NTQ0MTU2MDc4MDky.XrrRDw.8lnJHmI6PppEhtmM0tobD4zr840')
GUILD = ('Zeusbot90')

bot = commands.Bot(command_prefix='!')

@bot.command(name='Zeus', help='Responds with the Mighty Zeus')
async def Zeus_God(ctx):
    Zeus_God_Quotes = [
        'Im the Mighty Zeus!',
        (
            'Cool'),
        ]
    response = random.choice(Zeus_God_Quotes)
    await ctx.send(response)
@bot.command(name='date', help='Responds date and time')
async def date(ctx):
    now = datetime.now()
    date = now.strftime("%m/%d/%y, %H:%M:%S")
    response = date
    await ctx.send(response)


@bot.command(name = "JobSearch", help = "Responds with a search from Monster.com")
async def JobSearch (ctx,args1,args2):
        q = args1
        where = args2
        URL = ("https://www.monster.com/jobs/search/?q=%s&where=%s"% (q,where))
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id='ResultsContainer')
        response = URL
        await ctx.send (response)


        i = 0
        job_elems = results.find_all('section', class_='card-content')
        while i<1:
                for job_elem in job_elems: 
                        title_elem = job_elem.find('h2', class_='title')
                        company_elem = job_elem.find('div', class_='company')
                        location_elem = job_elem.find('div', class_ ='location')
                        if None in (title_elem, company_elem, location_elem):continue
                response1 = title_elem.text.strip()
                response2 = company_elem.text.strip()
                response3 = location_elem.text.strip()
                await ctx.send(response1)
                await ctx.send(response2)
                await ctx.send(response3)

                i=i+1


bot.run(TOKEN)

