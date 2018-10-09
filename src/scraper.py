import click

from display import display_message
from summary import printSummary
from scorecard import printScoreCard

if __name__ == '__main__':
	click.secho('Please enter the choices:')
	click.secho('Enter 1 to get the list of scores')
	click.secho('Enter 2 to get the Summary for a given channel')
	click.secho('Enter 3 to get the ScoreCard for a given channel')
	try:
		opt = click.prompt('Enter the option',type=int)
	except Exception:
		click.secho('Invalid Input!! Please try again')
		sys.exit()
	if opt == 1:
		display_message()
	elif opt == 2:
		ch = click.prompt('Enter the Channel number',type=int)
		printSummary(ch)
	else:
		ch = click.prompt('Enter the Channel number',type=int)
		printScoreCard(ch)