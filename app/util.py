from bs4 import BeautifulSoup
import csv
import time

timestr = time.strftime('%Y%m%d-%H%M%S')
sitemap_path = 'sitemap.xml'

def sitemap_parser(sitemap_path):
    with open(sitemap_path) as f:
        soup = BeautifulSoup(f, 'xml')
        link_str = soup.text[soup.text.find('https'):soup.text.find(']')]
        link_list = link_str.split('\n')
        return link_list
        
sitemap_parser(sitemap_path)

def link_writer(link_list):
    with open(f'output/links_{timestr}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for link in link_list:
            writer.writerow([link])

link_writer(sitemap_parser(sitemap_path))