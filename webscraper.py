from flask import Flask , render_template
app = Flask(__name__)

from bs4 import BeautifulSoup ## To import Beautiful soup for scraping
import requests ## To import requests

## Website which is needed to be scraped
url = "https://www.worldometers.info/coronavirus/"
req = requests.get(url)
bsObj = BeautifulSoup(req.text, "html.parser")

data=bsObj.find_all('div', class_="maincounter-number")
totalcases=data[0].text.strip()
recoveredcases = data[2].text.strip()

totalcases = int(totalcases.replace(',',''))
recoveredcases = int(recoveredcases.replace(',',''))

percentagerecovered = recoveredcases*100/totalcases
percentagerecovered = round(percentagerecovered,2)

@app.route('/')

def home():
	return render_template('home.html',totalcases=totalcases, percentagerecovered=percentagerecovered)

if __name__ == '__main__':
	app.run(debug=True)
