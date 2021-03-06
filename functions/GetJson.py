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
# @param    session
#           an object contain login credential
# @return 
def getJson(url, idContainer, session):
    print("Get JSON data...", end = "")
    soup = ParseUrl.parseUrl(url, session)
    # find tag which contains json link
    linkTag = soup.find('link', attrs={"type": "application/json"})
    # extract 100-record json link from attribute
    try:
        jsonLink = "https://library.osu.edu"
        jsonLink += linkTag.get('href')
    except:
        print("\nFail to find Json link!")
        print("Error when accessing: ", url)
        print("Hit enter to exit.")
        input()
        sys.exit()
    # open json link
    jsonPage = session.get(jsonLink)
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
