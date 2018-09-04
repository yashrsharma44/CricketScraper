from main import getPage, getHeader, getLinks, getScoreCard

def matchHeader(headers):
	
	matchHeader = [i for i in headers if i.find('h4', class_="cb-list-item ui-header ui-branding-header") is not None]
	match = [i.string for i in matchHeader]
	return match
