from main import getPage, getHeader, getLinks, getSummary, getScoreCard, getTestLinks
from utils import matchHeader
import click
from bs4 import BeautifulSoup as BS


@click.command()
def display_message():

	soup = getPage()
	headers = getHeader(soup)
	matches = matchHeader(headers)
	
	click.echo(click.style('The Live Matches Currently going on are :', fg='yellow'))
	for index,match in enumerate(matches):
		if index < 10:
			click.secho('0{} | {} '.format(index, match), fg='yellow')
		else:
			click.secho('{} | {} '.format(index, match), fg='yellow')
@click.command()
@click.option('--ch', default=1, help='Enter the channel number to display the summary')
def printSummary(ch):

	soup = getPage()
	links = getLinks(soup)
	headers = getHeader(soup)
	matches = matchHeader(headers)
	summary = list()
	scorecard = list()
	for i in links:
		try:
			summary.append(i.find_all('a')[1]['href'])
			scorecard.append(i.find_all('a')[2]['href'])
		except IndexError:
			pass
		
	
	data = getSummary(summary[ch-1])
	def iterator(data):
		for i in data:
			yield i

	gendata = iterator(data)
	click.secho('{}'.format(matches[ch-1]), fg='yellow')
	for index,i in enumerate(gendata):
		if index == int(len(data)/4):
			click.secho('------------------------------------', fg='red')
			click.secho('{}  |   {}'.format(i.string, next(gendata).string), fg='red')
		else:
			click.secho('{}  |   {}'.format(i.string, next(gendata).string), fg='red')

@click.command()
@click.option('--ch', default=1, help='Enter the channel number with --ch for scorecard')
def printScoreCard(ch):

	soup = getPage()
	links = getLinks(soup)

	link = links[ch-1].find_all('a')[2]['href']
	scorelinks = getTestLinks(link)
	
	if scorelinks:
		for link in scorelinks:
			data = getScoreCard(link)

			for player in data:
				details = player.strings
				try:
					click.secho('{}  |  {}({}) | {} | {} | {}'.format(next(details),next(details), next(details),next(details),next(details),next(details)), fg='red')
				except StopIteration:
					break
			click.secho('___________________________________' ,fg='red')

if __name__ == '__main__':
	printScoreCard()