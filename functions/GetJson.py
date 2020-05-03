import urllib.request
import requests
from bs4 import BeautifulSoup
import json
import sys
from functions import ParseUrl

# parse an url, find JSON link and extract results in a dict
# @param    url
#           an unparsed input url
# @param    idContainer
#           an container to store id
def getJson(url, idContainer):
    print("Get JSON data...", end = "")
    soup = ParseUrl.parseUrl(url)
    # find tag which contains json link
    linkTag = soup.find('link', attrs={"type": "application/json"})
    # extract 100-record json link from attribute
    jsonLink = "https://library.osu.edu"
    jsonLink += linkTag.get('href')
    # open json link
    jsonPage = requests.get(jsonLink)
    jsonContent = jsonPage.json()
    try:
        for tuple_ in jsonContent["docs"]:
            isInContainer = tuple_["id"] in idContainer
            if not isInContainer:
                idContainer.append(tuple_["id"])
        print("OK")
    except(ValueError, KeyError, TypeError):
        print("Fail to extract json data!")
    return soup
