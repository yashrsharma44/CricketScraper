import click
import sys

from display import display_message
from summary import printSummary
from scorecard import printScoreCard

if __name__ == '__main__':
	click.secho('Please enter the choices:',fg='red')
	click.secho('Enter 1 to get the list of scores',fg='green')
	click.secho('Enter 2 to get the Summary for a given channel',fg='green')
	click.secho('Enter 3 to get the ScoreCard for a given channel',fg='green')
	try:
		opt = click.prompt('Enter the option',type=int)
	
		if opt == 1:
			display_message()
		elif opt == 2:
			ch = click.prompt('Enter the Channel number',type=int)
			printSummary(ch)
		elif opt==3:
			ch = click.prompt('Enter the Channel number',type=int)
			printScoreCard(ch)
		else:
			raise Exception
	except Exception:
		click.secho('Invalid Input!! Please try again',fg='red')
		sys.exit()