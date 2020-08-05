import urllib.request
from bs4 import BeautifulSoup

def loadUrlSession(session, url):
    html = session.get(url)
    return html

# parse url link to readable bs4 content
# @param    url
#           The url needed to be parsed
# @param    session
#           The object which contain login credential
# @return   soup
#           parsed url
def parseUrl(url, session):
    print("Reading url...", end = "")
    html = loadUrlSession(session, url)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup
