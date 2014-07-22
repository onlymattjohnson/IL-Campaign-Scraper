from bs4 import BeautifulSoup
import urllib2

def get_rss_links(data):
    soup = BeautifulSoup(data)

    for link in soup.find_all('link'):
        print link.text

def get_url_contents(url):
    response = urllib2.urlopen(url)
    html = response.read()

    return html

url = 'http://www.elections.il.gov/rss/SBEReportsFiledWire.aspx'
url_contents = get_url_contents(url)

get_rss_links(url_contents)
