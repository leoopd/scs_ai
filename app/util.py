from bs4 import BeautifulSoup
import csv
import time
import requests
import re
import os

timestr = time.strftime('%Y%m%d-%H%M%S')
sitemap_path = 'sitemap.xml'
csv_file = 'links_20230406-235607.csv'
folder_path = 'html'

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
            with open(f'html/{name}.html', 'w') as h:
                h.write(response.text)

# html_grabber(csv_file)

def text_parser(file_path):
    with open(file_path) as f:
        soup = BeautifulSoup(f, 'html.parser')
        article = soup.find('article')
        if article:
            article = article.text

            # Removes occurrences of punctuation (preserves one occurrence), removes extra spaces
            # and inserts the missing spaces between words (can contain äöüßÜÖÄ) and after punctuation.
            final_article = re.sub(r'([^\w\s])\1+', r'\1 ', article)
            final_article = re.sub(r'(\s+)([^\w\s])*\s*', r'\2 ', final_article)
            final_article = re.sub(r'(?<=[.,?!])(?=[^\s\d])(?!$)|(?<=[a-zäöüß])(?=[A-ZÜÖÄ])', r' ', final_article)

            return article
        else:
            return ''

def parsing_folder_content(folder_path):
    articles = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        article = text_parser(file_path)
        if article:
            articles.append(article)
    return articles

def articles_to_csv(articles):
    with open(f'csv/artiles_{timestr}.csv', 'w') as f:
        writer = csv.writer(f, delimiter='#')
        writer.writerow(['Category', 'Problem', 'Article'])
        for article in articles:
            writer.writerow([article])

articles_to_csv(parsing_folder_content(folder_path))