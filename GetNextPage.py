import ParseUrl
from bs4 import BeautifulSoup
import ParseUrl

# find url for next page and return it
# @param    url
#           current unparsed page url
# @return   nextUrl
#           next page's url. If it is the last page,return None
def getNextPage(url):
    nextUrl = "https://library.osu.edu"
    soup = ParseUrl.parseUrl(url)
    aTag= soup.find('a', attrs={"rel": "next"})
    if aTag != None:
        nextUrl += aTag.get('href')
    else:
        nextUrl == None
    return nextUrl
