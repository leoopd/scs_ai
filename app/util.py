from bs4 import BeautifulSoup
import csv

sitemap_path = 'sitemap.xml'

def sitemap_parser(sitemap_path):
    with open(sitemap_path) as f:
        soup = BeautifulSoup(f, 'xml')
        link_str = soup.text[soup.text.find('https'):soup.text.find(']')]
        link_list = link_str.split('\n')
        return link_list
        
sitemap_parser(sitemap_path)

def placeholder():
    with open('output/links.csv') as f:
        reader = csv.reader(f)