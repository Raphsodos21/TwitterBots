import requests
import tweepy
from bs4 import BeautifulSoup
import locale
import json
from datetime import date, timedelta



api_key="***********************"
api_key_secret="***********************"
access_token="***********************"
access_token_secret="***********************"

auth=tweepy.OAuthHandler(consumer_key=api_key,consumer_secret=api_key_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
keywords = ["allah", "musulman", "mahomet", "islamogauchisme", "coran", "sharia", "charia", "imam", "jihad", "halal", "voile", "burkini", "islamique", "islamisme", "islamo", "islamophobe", "sourate", "mosquée","Allah", "Islam", "Musulman", "Mahomet", "Islamogauchisme", "Coran", "Sharia", "Charia", "Imam", "Jihad", "Halal", "Voile", "Burkini", "Islamique", "Islamisme", "Islamo", "Islamophobe", "Sourate", "Mosquée","niqab","Niqab"]

france_woeid=23424819

trend_result = api.trends_place(id = france_woeid)
danger=False
matches=""

for trend in trend_result[0]["trends"][:20]:
 	
 	if any(x in trend["name"] for x in keywords):
 		print(trend["name"])
 		danger=True
 		matches = matches + trend["name"] +" "

if danger:
	api.update_status("Attention, les tendances Twitter en France contiennent les termes "+ matches +".\nSi vous êtes musulman, veuillez eviter Twitter aujourd'hui, les islamophobes risquent d'être trop présents.")
