from utils import getPage, getHeader, getLinks, getSummary, getScoreCard, getTestLinks, finalScore,matchHeader 
import click
import sys
from bs4 import BeautifulSoup as BS
import scorecard


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
	
	#click.secho('{}\n'.format(matches[ch]), fg='yellow')

	for index,i in enumerate(gendata):
		if index == int(len(data)/4):
			click.secho(' __________________________________________', fg='red')
			click.secho(' {}     {}'.format(i.string, next(gendata).string), fg='red')
		else:
			run = next(gendata).string
			click.secho(' {}'.format(i.string)+' '*(20-len(i.string))+'|{}'.format(run), fg='red')

if __name__ == '__main__':
	printSummary()