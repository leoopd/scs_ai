from bs4 import BeautifulSoup
import csv
import time
import requests
import re

timestr = time.strftime('%Y%m%d-%H%M%S')
sitemap_path = 'sitemap.xml'
csv_file = 'links_20230406-235607.csv'

def sitemap_parser(sitemap_path):
    with open(sitemap_path) as f:
        soup = BeautifulSoup(f, 'xml')
        link_str = soup.text[soup.text.find('https'):soup.text.find(']')]
        link_list = link_str.split('\n')
        return link_list

def link_writer(link_list):
    with open(f'links_{timestr}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for link in link_list:
            writer.writerow([link])

# link_writer(sitemap_parser(sitemap_path))

def html_grabber(csv_file):
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            link = row[0]
            name = link[26:].replace('/', '_')
            response = requests.get(link)
            with open(f'output/{name}.html', 'w') as h:
                h.write(response.text)

# html_grabber(csv_file)

def text_parser(file_path):
    with open(file_path) as f:
        soup = BeautifulSoup(f, 'html.parser')
        article = soup.find_all('article')

        # Removes occurrences of punctuation (preserves one occurrence), removes extra spaces
        # and inserts the missing spaces between words (can contain äöüßÜÖÄ) and after punctuation.
        article = re.sub(r'([^\w\s])\1+', r'\1 ', article.text)
        article = re.sub(r'(\s+)([^\w\s])*\s*', r'\2 ', article)
        article = re.sub(r'(?<=[.,?!])(?=[^\s\d])(?!$)|(?<=[a-zäöüß])(?=[A-ZÜÖÄ])', r' ', article)
        
        return article

text_parser('output/cloud-speicher_2-Faktor-Authentifizierung_.html')