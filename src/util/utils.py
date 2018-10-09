import requests

from bs4 import BeautifulSoup as BS


def matchHeader(headers):
	'''
	Returns the list of match header
	'''	
	matchHeader = [i for i in headers if i.find('h4', class_="cb-list-item ui-header ui-branding-header") is not None]
	match = [i.string for i in matchHeader]
	return match


def getPage():
	'''
	Generates a Beautiful Soup, of cricket scorecard
	'''
	page = requests.get("https://m.cricbuzz.com/cricket-match/live-scores")
	soup = BS(page.content, 'html.parser')
	return soup

def getHeader(soup):
	'''
	Lists out the list of header
	'''
	header = soup.find_all('div', class_="list-group")
	return header

def getLinks(soup):
	'''
	Gets the links of summary and scorecard
	'''
	links = soup.find_all('div', class_="btn-group cbz-btn-group")
	return links

def getScoreCard(link):
	'''
	Returns the data, containing the scorecard
	'''
	link = "https://m.cricbuzz.com"+link
	page = requests.get(link)
	soup = BS(page.content, 'html.parser')
	tabledata = soup.find_all('tr', class_="active")
	return tabledata

def getSummary(link):
	'''
	Returns the data containing the Summary
	'''
	link = "https://m.cricbuzz.com"+link
	page = requests.get(link)
	soup = BS(page.content, 'html.parser')
	tabledata = soup.find_all('td', class_="cbz-grid-table-fix")
	return tabledata

def getTestLinks(link):
	'''
	Returns the links of Test matches. As test matches have 4 scorecards, so returns 4 links
	'''
	soup = getScorePage(link)
	links = getLinks(soup)
	scores = links[1].find_all('a')
	scorelink = [i['href'] for i in scores]

	return scorelink

def getScorePage(link):
	'''
	Returns the web page containing the scorecard
	'''
	page = requests.get('https://m.cricbuzz.com/'+link)
	soup = BS(page.content, 'html.parser')
	return soup

def finalScore(link):
	'''
	Returns the data containing the total score of a team
	'''
	soup = getScorePage(link)
	obj = soup.find_all('div', class_="cb-list-item")[2].strings
	return obj


