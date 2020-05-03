import sys
import json
import csv
import re
import urllib.request
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import Category_list
import GetCollectionName
import GetJson
import GetMaxRecords
import GetNextPage
import ParseUrl
import ReadCSV
import WriteCSV
        
def main():
    pageUrl = []
    csvCategory = []
    idList = []
    idListCombine = []
    outputList = []
    httpSuffix = "https://library.osu.edu/dc/concern/generic_works/"
    i = 0
    iter_ = 0
    remainRecords = 0
    
    # get inputfile
    print("Please enter csv file name. The file must in the same folder with your main.py program: ")
    fileIn = input()
    
    # get outputfile
    print("Please enter output file name: ")
    fileOut = input()
    try:
        pageUrl = ReadCSV.readCSV(fileIn)
    except:
        print("Fail to open this file. Press enter to exit.")
        key = input()
        sys.exit()
        
    numOfUrl = len(pageUrl)
    print("There are ", numOfUrl, " records in the input file.")
    # id scraping
    for url in pageUrl:
        # parse url
        print("Reading url...", end = "")
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
        print("OK")
        # after get that link, read json data from it
        while remainRecords > 0:
            print("Get JSON data...", end = "")
            GetJson.getJson(nextLink, idList)
            print("OK")
            print("Find rest of JSON page for this link...", end = "")
            nextPage = GetNextPage.getNextPage(nextLink)
            nextLink = nextPage
            print("OK. Remaining records for this link: ", end = "")
            remainRecords = numOfRecords - len(idList)
            print(remainRecords)
            print("Number of id scrapped: ", len(idList))
        i += 1
        print("Create identifier links...", end = "")
        while iter_ < len(idList):
            newID = httpSuffix + idList[0]
            idList.append(newID)
            idList.pop(0)
            iter_ += 1
        iter_ = 0
        idList.insert(0, collectionTitle)
        print("OK")
        print(i, "/", len(pageUrl), " has been processed.")
        idListCombine.append(idList)
        idList = []
        
    # write data to csv file
    WriteCSV.writeCSV(idListCombine, fileOut)
    
    # program exit
    print("The program has finished. The output file is: ", fileOut, " . It is located in the same folder with your main.py program. Press enter to exit.")
    key = input()
    sys.exit()
    
if __name__ == "__main__":
    main()
