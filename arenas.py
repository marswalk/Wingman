import os
import requests
import json
from datetime import datetime

TOKEN = os.environ['TOKEN']
APIKEY = os.environ['APIKEY']

def get_armap():
  response = requests.get(f"https://api.mozambiquehe.re/maprotation?version=2&auth={APIKEY}")
  json_data = response.json()
  print(datetime.now(), ": arenas map rotation requested")
  map = json_data['arenas']['current']['map']
  time = json_data['arenas']['current']['remainingTimer']
  image = json_data['arenas']['current']['asset']
  nextmap = json_data['arenas']['next']['map']
  return(map, time, image, nextmap)