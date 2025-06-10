import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

class Quotes:
    def __init__(self, url, pages):
        self.url = url
        self.pages = pages
        self.data = []

    def fetch_page(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.span.text
            author = quote.small.text
            self.data.append([text, author])

    def scrape(self):
        for ind in range(1, self.pages + 1):
            html = self.fetch_page(f"{self.url}/page/{ind}/")
            if html:
                self.parse_page(html)
            time.sleep(randint(1, 3))

    def get_data(self):
        return self.data
    
    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Quote', 'Author'])
            writer.writerows(self.data)




