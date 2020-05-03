import csv

# open csv file and read handler link, store in a list
# @param    csvName
#           the file name user typed in
# @return   urlList
#           a list contain item url that need to be scraped
def readCSV(csvName):
    urlList = []
    inFile = open(csvName, 'r')
    csvReader = csv.reader(inFile, delimiter=',')
    for row in csvReader:
        urlList.append(row[0])
    # del the column name read for first line
    urlList.pop(0)
    return urlList
