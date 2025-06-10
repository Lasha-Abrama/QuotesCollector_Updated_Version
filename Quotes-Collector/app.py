from flask import Flask, render_template, send_file
from quotes import Quotes
import os

app = Flask(__name__)
scraper = Quotes('https://quotes.toscrape.com', 2)
scraper.scrape()
data = scraper.get_data()

@app.route('/')
def index():
    return render_template('index.html', quotes=data)

@app.route('/download')
def download():
    filename = 'quotes.csv'
    scraper.save_to_csv(filename)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
