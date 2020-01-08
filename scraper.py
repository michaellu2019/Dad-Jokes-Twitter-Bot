import requests
from bs4 import BeautifulSoup as bs
import os

# dad jokes url
url = 'https://www.boredpanda.com/funny-dad-jokes-puns/?utm_source=google&utm_medium=organic&utm_campaign=organic'

# parses webpage into BeautifulSoup object
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# find all elements containing jokes
jokes = []
spans = soup.findAll('span', attrs = {'class': 'bordered-description'})

# save all jokes in an array
for span in spans:
	try:
		joke = span.text
		jokes.append(joke)
	except Exception as ex:
		print('exception occurred: ', ex)

# write jokes from array into a file
f = open('dad_jokes.txt', 'w')

for joke in jokes:
	f.write(joke + '\n')

f.write('That\'s all the dad jokes I have for now... Please like, comment, and subscribe...\n')
f.close()
print('webpage scraped and jokes stored in dad_jokes.txt')