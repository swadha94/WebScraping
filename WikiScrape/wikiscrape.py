from flask import Flask, render_template
app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
#import pandas as pd

url = 'https://en.m.wikipedia.org/wiki/List_of_largest_Internet_companies'
req = requests.get(url)
bsObj = BeautifulSoup(req.text, 'html.parser')
data = bsObj.find('table', {'class' : 'wikitable sortable mw-collapsible jquery-tablesorter'})

table_data = []
trs = bsObj.select('table tr')
for tr in trs[1:6]:
	row = []
	for t in tr.select('td')[:3]:
		row.extend([t.text.strip()])
	table_data.append(row)
data=table_data

@app.route('/')

def home():
	return render_template('wikihome.html', data=data)

if __name__ == '__main__':
	app.run(debug=True)	