from bs4 import BeautifulSoup
from functions import Category_list

# get the name of this collection
# @param    soup
#           a parsed url
# @return   collectionName
def getCollectionName(soup):
    collectionName = ""
    for categoryName in Category_list.categoryList: 
        name = soup.find('input', attrs = {"type" : "hidden", "name" : categoryName})
        if name != None:
            collectionName += name.get("value")
    return collectionName
