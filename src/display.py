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

if __name__ == '__main__':
	display_message()