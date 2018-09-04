from utils import getPage, getHeader, getLinks, getSummary, getScoreCard, getTestLinks, finalScore,matchHeader 
import click
import sys
from bs4 import BeautifulSoup as BS


@click.command()
def display_message():
	'''
	This method displays the list of live matches going on
	'''
	'''
	Arguments
	---------
	None

	Returns
	-------
	None : List of live matches
	'''

	soup = getPage()
	headers = getHeader(soup)
	matches = matchHeader(headers)
	
	click.echo(click.style('The Live Matches Currently going on are :', fg='yellow'))
	for index,match in enumerate(matches):
		if index+1 <10:
			click.secho('0{} | {} '.format(index+1, match), fg='yellow')
		else:
			click.secho('{} | {} '.format(index+1, match), fg='yellow')
@click.command()
@click.option('--ch', default=1, help='Enter the channel number with --ch to display the summary')
def printSummary(ch):
	'''
	This method takes a channel number,
	and returns the summary of the match
	'''
	'''
	Arguments
	---------
	int : channel number

	Returns
	-------
	None : Output
	'''

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
	click.secho('{}\n'.format(matches[ch-1]), fg='yellow')
	for index,i in enumerate(gendata):
		if index == int(len(data)/4):
			click.secho(' __________________________________________', fg='red')
			click.secho(' {}     {}'.format(i.string, next(gendata).string), fg='red')
		else:
			run = next(gendata).string
			click.secho(' {}'.format(i.string)+' '*(20-len(i.string))+'|{}'.format(run), fg='red')

@click.command()
@click.option('--ch', default=1, help='Enter the channel number with --ch for scorecard')
def printScoreCard(ch):
	'''
	This method takes in a channel number,
	and returns the Scorecard for a given
	match number
	'''
	'''
	Arguments
	---------
	int : Channel number

	Returns
	-------
	None : Displays the output
	'''

	soup = getPage()
	links = getLinks(soup)
	
	headers = getHeader(soup)
	matches = matchHeader(headers)
	try:
		link = links[ch-1].find_all('a')[2]['href']
		scorelinks = getTestLinks(link)
	except IndexError:
		click.secho('Score Card not Available !!',fg='red')
		sys.exit()	
	click.secho('{}'.format(matches[ch-1]), fg='yellow')
	
	for link in scorelinks:
		data = getScoreCard(link)
		displayline=None
		click.secho(' Batsman            |   R(B)     | 4 | 6   | S/R',fg='blue')
		for player in data:
			details = player.strings
			
			try:
				name = next(details)
				run = next(details)
				ball = next(details)
				four = next(details)
				six = next(details)
				sr = next(details)
				text = '{}'.format(name)+' '*(20-len(name))+'| {}({})'.format(run,ball)\
				+' '*(9-len(run)-len(ball))+'| {} | {} '.format(four,six)+' '*(4-len(four)-len(six))+'| {}'.format(four,six,sr)
				click.secho(text, fg='red')
			except StopIteration:
				break
		click.secho('_'*(len(text)), fg='red')
		score = finalScore(link)
		
		for details in score:
			click.secho(' {} '.format(details), fg='red')
		click.secho('_'*(len(text)) ,fg='red')

if __name__ == '__main__':
	printScoreCard()