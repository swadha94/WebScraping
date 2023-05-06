from flask import Flask , render_template

app = Flask(__name__)


from bs4 import BeautifulSoup ## To import Beautiful soup for scraping
import requests ## To import requests


## Website which is needed to be scraped
source = requests.get('http://quotes.toscrape.com').text
soup = BeautifulSoup(source,'lxml')


quote = soup.find('div', class_='quote')	#finding first quote text
quotetext = quote.span.text
print(quotetext)

author = soup.find('small' , class_= 'author') #finding the first author
authortext = author.text 
print(authortext)

@app.route('/')

def home():
	return render_template('home.html', quotetext = quotetext , authortext = authortext)


if __name__ == '__main__':
	app.run(debug=True)
