from bs4 import BeautifulSoup
import csv
import time
import requests

sitemap_path = 'sitemap.xml'
timestr = time.strftime('%Y%m%d-%H%M%S')

def sitemap_parser(sitemap_path):
    '''
    Extracts the links from the STRATO FAQ sitemap and bundles them in a list that gets returned.
    '''
    with open(sitemap_path) as f:
        soup = BeautifulSoup(f, 'xml')
        link_str = soup.text[soup.text.find('https'):soup.text.find(']')]
        link_list = link_str.split('\n')
        return link_list

def link_writer(link_list):
    '''
    Writes the link list returned by sitemap_parser() to a csv.
    '''
    with open(f'links_{timestr}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for link in link_list:
            writer.writerow([link])

# link_writer(sitemap_parser(sitemap_path))

def html_grabber(csv_file):
    '''
    Reads the csv returned by link_writer, downloads each webpage and saves it as an html file in /html.
    '''
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            link = row[0]
            name = link[26:].replace('/', '_')
            response = requests.get(link)
            with open(f'html/{name}.html', 'w') as h:
                h.write(response.text)

# html_grabber(csv_file)