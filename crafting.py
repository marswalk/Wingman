import os
import requests
import json
from datetime import datetime

TOKEN = os.environ['TOKEN']
APIKEY = os.environ['APIKEY']

def get_crafting():
  response = requests.get(f"https://api.mozambiquehe.re/crafting?auth={APIKEY}")
  json_data = response.json()
  print(datetime.now(), ": crafting rotation requested")
  dailybundle = json_data[0]['bundle']
  weeklybundle = json_data[1]['bundle']
  
  daily1 = json_data[0]['bundleContent'][0]['itemType']['name']
  dailyicon1 = json_data[0]['bundleContent'][0]['itemType']['asset']
  daily2 = json_data[0]['bundleContent'][1]['itemType']['name']
  dailyicon2 = json_data[0]['bundleContent'][1]['itemType']['asset']

  weekly1 = json_data[1]['bundleContent'][0]['itemType']['name']  
  weeklyicon1 = json_data[1]['bundleContent'][0]['itemType']['asset']
  weekly2 = json_data[1]['bundleContent'][1]['itemType']['name']
  weeklyicon2 = json_data[1]['bundleContent'][1]['itemType']['asset']
  
  return(dailybundle, daily1, daily2, dailyicon1, dailyicon2, weeklybundle, weekly1, weekly2, weeklyicon1, weeklyicon2)