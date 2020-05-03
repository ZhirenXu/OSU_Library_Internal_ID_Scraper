from functions import ParseUrl
from functions import GetCollectionName
from functions import GetMaxRecords
from functions import GetJson
from functions import GetNextPage
from functions import CreateIDList

##Main function of ID scrapper
# @param    urlList
#           A list of url that need to be processed
# @param    idList
#           A list that contain Json ID

def runProcess(urlList, idList):
    idListCombine = []
    i = 0
    j = 0
    
    for url in urlList:
        # parse url
        parsedUrl = ParseUrl.parseUrl(url)
        # find the name of collection
        collectionTitle = GetCollectionName.getCollectionName(parsedUrl)
        # find how many records in this collection
        tag = parsedUrl.find('meta', attrs={'name': "totalResults"})
        numOfRecords = int(tag['content'])
        remainRecords = numOfRecords
        # find 100-per-page link
        maxRecordLink = GetMaxRecords.getMaxRecords(parsedUrl)
        nextLink = maxRecordLink
        # after get that link, read json data from it
        while remainRecords > 0:
            parsedNextLink = GetJson.getJson(nextLink, idList)
            nextPage = GetNextPage.getNextPage(parsedNextLink)
            nextLink = nextPage
            remainRecords = numOfRecords - len(idList)
            print(remainRecords)
            print("Number of id scrapped: ", len(idList))
        i += 1
        idListCombine = CreateIDList.createIDList(i, j, idList, idListCombine)
        idList = []
        print(i, "/", len(urlList), " has been processed.")
    return idListCombine
