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
    
    outFile = open(outputFile, 'w', encoding = 'utf8', newline='')
    csvWriter = csv.writer(outFile)
    # zip subList so csvWriter will written in coloum
    for subList in combinedList:
        zippedList = zip_longest(subList, fillvalue = '')
        # write all ids into file
        print("Writing identifiers into ", outputFile, "...")
    #open file for output
        try:
            csvWriter.writerows(zippedList)
        except:
            print("Fail to write csv!")
    print("Complete!")
    outFile.close()
