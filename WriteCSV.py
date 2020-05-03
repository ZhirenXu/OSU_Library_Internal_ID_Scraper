import sys
import csv
from itertools import zip_longest

# write category and data into csv file
# @param    combinedList
#           a list contains idList from each url
# @param    outputFile
#           output File pointed by user
def writeCSV(combinedList, outputFile):
    zippedList = []
    # zip idList in combinedList for output
    zippedList = zip_longest(*combinedList, fillvalue = '')
    # write all ids into file
    print("Writing identifiers into ", outputFile, "...")
    #open file for output
    try:
        outFile = open(outputFile, 'w', encoding = 'utf8', newline='')
        csvWriter = csv.writer(outFile)
        for element in zippedList:
            csvWriter.writerow(element)
        print("Complete!")
        outFile.close()
    except:
        print("Fail to write csv!")
