import csv
from bs4 import BeautifulSoup
import time
import re
import os

csv_file = 'links_20230406-235607.csv'
folder_path = 'html'
timestr = time.strftime('%Y%m%d-%H%M%S')

def text_parser(file_path):
    '''
    Extracts the text-body of the given STRATO FAQ and returns it.
    Returns an empty string if not possible.
    '''
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

            return final_article
        else:
            return ''

def parsing_folder_content(folder_path):
    '''
    Calls text_parser() on every file in the specified folder, extracts category and title from the filename
    and bundles it up in list that gets returned.
    '''
    articles = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        category = filename[:filename.find('_')].capitalize()
        title = filename[filename.find('_')+1:filename.find('.')].replace('-', ' ').strip('_')
        article = text_parser(file_path)
        if article:
            articles.append([category, title, article])
    return articles

def articles_to_csv(articles, dest_folder='faq_contents/'):
    '''
    Writes the list returned by parsing_folder_content() to a csv.
    '''
    with open(f'csv/artiles_{timestr}.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='#')
        writer.writerow(['Category', 'Title', 'Article'])
        for article in articles:
            writer.writerow([article[0], article[1], article[2]])

articles_to_csv(parsing_folder_content(folder_path))