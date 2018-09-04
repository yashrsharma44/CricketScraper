from utils import getPage, getHeader, getLinks, getSummary, getScoreCard, getTestLinks, finalScore,matchHeader 
import click
import sys
from bs4 import BeautifulSoup as BS

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
