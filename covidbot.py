import requests
import tweepy
from bs4 import BeautifulSoup
import locale
import json
from datetime import date, timedelta

URL = "https://www.worldometers.info/coronavirus/country/morocco/"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html5lib")
infos = soup.findAll("div", {"class": "maincounter-number"})
totalcases = infos[0].find("span").text
deaths = infos[1].find("span").text
recovered = infos[2].find("span").text

totalcases = int(totalcases.replace(",", ""))
deaths = int(deaths.replace(",", ""))
recovered = int(recovered.replace(",", ""))
activecases = totalcases- deaths - recovered

today = date.today() - timedelta(1)
dayid ="newsdate"+ today.strftime("%Y-%m-%d")
todaycases = soup.find("div", {"id": dayid}).find("li", {"class": "news_li"}).text
todaycases = todaycases[:-9]

print(totalcases)
print(deaths)
print(recovered)
print(activecases)
print(todaycases)


api_key="***********************"
api_key_secret="***********************"
access_token="***********************"
access_token_secret="***********************"

auth=tweepy.OAuthHandler(consumer_key=api_key,consumer_secret=api_key_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth,wait_on_rate_limit=True)

api.update_status(today.strftime("%d/%m/%Y") +"\n\n" +todaycases +"\nTotal Covid-19 Cases : "+ '{:,}'.format(totalcases)+"\nTotal Deaths : "+ '{:,}'.format(deaths)+"\nTotal recovered : "+'{:,}'.format(recovered)+"\nActive Cases : "+'{:,}'.format(activecases)+"\n\n#COVID")