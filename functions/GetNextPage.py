from bs4 import BeautifulSoup
from functions import ParseUrl

# find url for next page and return it
# @param    url
#           current parsed page url
# @return   nextUrl
#           next page's url. If it is the last page,return None
def getNextPage(parsedUrl):
    nextUrl = "https://library.osu.edu"
    
    print("Find rest of JSON page for this link...", end = "")
    #soup = ParseUrl.parseUrl(url)
    aTag= parsedUrl.find('a', attrs={"rel": "next"})
    if aTag != None:
        nextUrl += aTag.get('href')
    else:
        nextUrl == None
    print("OK. Remaining records for this link: ", end = "")
    return nextUrl
