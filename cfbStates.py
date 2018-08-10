from bs4 import BeautifulSoup
import requests
import re

def getTeamInfo(teamlink):
	page = requests.get(teamlink)
	content = page.content
	soup = (BeautifulSoup(content, "html.parser"))
	teamSection = soup.find("div", {"class": "row-fluid matchupslist row4"})
	eachTeam = teamSection.find_all("li")
	for team in eachTeam:
		teamDiv = team.div
		if(teamDiv['data-conference'] != "NON-FBS TEAMS"):
			#GET STATE OF TEAM
			#ADD DATA
			#print(teamDiv['data-name'] + ' ' + teamDiv['data-winscount'] + ' ' + teamDiv['data-lossescount'] + ' ' + teamDiv['data-tiescount'])
			


if __name__ == "__main__":
	soup = BeautifulSoup(open("teampage.html"), "html.parser")
	teams = soup.find_all("li", "span4") + soup.find_all("li", "span3")
	teamURLs = []
	for li in teams:
		li = str(li)
		teampage = re.search('href="(.*)">', li)
		teamURLs.append(teampage.group(1))
	getTeamInfo(teamURLs[0])
	