import os
import requests
import json
from datetime import datetime

TOKEN = os.environ['TOKEN']
APIKEY = os.environ['APIKEY']

def get_brmap():
  response = requests.get(f"https://api.mozambiquehe.re/maprotation?version=2&auth={APIKEY}")
  json_data = response.json()
  print(datetime.now(), ": br map rotation requested")
  map = json_data['battle_royale']['current']['map']
  time = json_data['battle_royale']['current']['remainingTimer']
  image = json_data['battle_royale']['current']['asset']
  nextmap = json_data['battle_royale']['next']['map']
  return(map, time, image, nextmap)