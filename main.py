import discord
import os
import requests
import json
from datetime import datetime
import logging

from battleroyale import get_brmap
from arenas import get_armap
from crafting import get_crafting


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

r = requests.get("https://discord.com/api/v7/users/@me")
print(r.text)

TOKEN = os.environ['TOKEN']
APIKEY = os.environ['APIKEY']

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = response.json()
  print(json_data)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='$help'))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$help'):
    await message.channel.send('I am still in development lol')
    await message.channel.send('```Try $map or $crafting?```')

  if message.content.startswith('$map'):
    await message.channel.send('V3.0 adds support for arenas map')
    await message.channel.send('Try `$brmap` or `$armap`')

  if message.content.startswith('$brmap'):
    map, time, image, nextmap = get_brmap()
    embed=discord.Embed(title="BR Map Rotation", color=0x109319)
    embed.add_field(name="Current map: ", value=map)
    embed.add_field(name="Time remaining: ", value=time)
    embed.set_image(url=image)
    embed.add_field(name="Next map: ", value=nextmap, inline=False)
    embed.set_footer(text="Wingman Bot by Marswalk")
    await message.channel.send(embed=embed)

  if message.content.startswith('$armap'):
    map, time, image, nextmap = get_armap()
    embed=discord.Embed(title="Arenas Map Rotation", color=0x109319)
    embed.add_field(name="Current map: ", value=map)
    embed.add_field(name="Time remaining: ", value=time)
    embed.set_image(url=image)
    embed.add_field(name="Next map: ", value=nextmap, inline=False)
    embed.set_footer(text="Wingman Bot by Marswalk")
    await message.channel.send(embed=embed)

  if message.content.startswith('$crafting'):
    dailybundle, daily1, daily2, dailyicon1, dailyicon2, weeklybundle, weekly1, weekly2, weeklyicon1, weeklyicon2 = get_crafting()
    
    embed=discord.Embed(title="Daily / Weekly Crafting Rotation", color=0x109319)
    embed.add_field(name="Daily bundle: ", value=dailybundle)
    embed.add_field(name="Weekly bundle: ", value=weeklybundle)
    embed.set_footer(text="Wingman Bot by Marswalk")
    await message.channel.send(embed=embed)
    
    embed=discord.Embed()
    embed.set_author(name=daily1, icon_url=dailyicon1)
    await message.channel.send(embed=embed)
    embed=discord.Embed()
    embed.set_author(name=daily2, icon_url=dailyicon2)
    await message.channel.send(embed=embed)
    
    embed=discord.Embed()
    embed.set_author(name=weekly1, icon_url=weeklyicon1)
    await message.channel.send(embed=embed)
    embed=discord.Embed()
    embed.set_author(name=weekly2, icon_url=weeklyicon2)
    await message.channel.send(embed=embed)


  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(os.getenv('TOKEN'))