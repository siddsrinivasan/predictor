import requests
from bs4 import BeautifulSoup
import datetime



get_upcoming():
	#Get the new upcoming matches:

	url = 'https://projects.fivethirtyeight.com/soccer-predictions/premier-league/'
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')

	matches = []
	upcoming = soup.find('div', class_="match-container initial-view")
	while (upcoming!= None):
		try:
			team1 = upcoming['data-team1']
			team2 = upcoming['data-team2']
			match = (team1,team2)
			matches.append(match)
			upcoming = upcoming.next_sibling
		except:
			upcoming = None
	# Currently it only grabs the pairs for the next month (so January)

get_results():
	# Results:
	url = 'https://www.premierleague.com/results'
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')


class Team(object):
    name = ""
    position = 0
    wins = 0
    ties = 0
    losses = 0
    home_wins = 0
    home_losses = 0
    home_ties = 0
    away_wins = 0
    away_losses = 0
    away_ties = 0
    gpg = 0.0
    home_gpg = 0.0
    away_gpg = 0.0

    # The class "constructor" - It's actually an initializer 
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

def make_team(name,position,wins,ties,losses):
    student = Student(name, age, major)
    return team


get_results




