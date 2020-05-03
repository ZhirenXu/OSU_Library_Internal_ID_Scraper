from bs4 import BeautifulSoup

# get 100-per-page link from input url
# @param    soup
#           parsed url from input file
# @return   maxRecordLink
#           an unparsed 100-per-page url
def getMaxRecords(soup):
    maxRecordLink = "https://library.osu.edu"
    aTagList = soup.find_all('a')
    for aTag in aTagList:
        if '100' in aTag.contents:   
            href = aTag.get('href')
            if href != None:
                maxRecordLink += href
                break
    print("OK")
    return maxRecordLink
