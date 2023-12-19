import requests
from bs4 import BeautifulSoup
import json

class WebPageScraper:
    def __init__(self, url):
        self.url = url
        self.news_data = {}

    def fetch_content(self):
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def get_data(self):
        headline = self.soup.find('h1', itemprop='headline')
        if headline:
            self.news_data['headline_text'] = headline.get_text(strip=True)

        paragraphs = self.soup.find_all('p')
        paragraph_texts = [p.get_text(separator=' ', strip=True) for p in paragraphs]
        self.news_data['content_text'] = paragraph_texts

    def store_data(self, file):
        json_data = json.dumps(self.news_data, indent=4)
        with open(file, 'w') as file:
            file.write(json_data)
        print("Json Data ",json_data)
        print(f"Data saved to {file}")

news_web_url= 'https://indianexpress.com/article/india/parliament-winter-session-2023-live-news-updates-stalement-9072430/'
scraper = WebPageScraper(news_web_url)
scraper.fetch_content()
scraper.get_data()
scraper.store_data('news_data.json')

