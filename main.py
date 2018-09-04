from bs4 import BeautifulSoup as BS
import requests

def getPage():
	page = requests.get("https://m.cricbuzz.com/cricket-match/live-scores")
	soup = BS(page.content, 'html.parser')
	return soup

def getHeader(soup):
	header = soup.find_all('div', class_="list-group")
	return header

def getLinks(soup):
	links = soup.find_all('div', class_="btn-group cbz-btn-group")
	return links

def getScoreCard(link):
	link = "https://m.cricbuzz.com"+link
	page = requests.get(link)
	soup = BS(page.content, 'html.parser')
	tabledata = soup.find_all('tr', class_="active")
	return tabledata

def getSummary(link):
	link = "https://m.cricbuzz.com"+link
	page = requests.get(link)
	soup = BS(page.content, 'html.parser')
	tabledata = soup.find_all('td', class_="cbz-grid-table-fix")
	return tabledata

def getTestLinks(link):
	soup = getScorePage(link)
	links = getLinks(soup)
	scores = links[1].find_all('a')
	scorelink = [i['href'] for i in scores]

	return scorelink

def getScorePage(link):
	page = requests.get('https://m.cricbuzz.com/'+link)
	soup = BS(page.content, 'html.parser')
	return soup
