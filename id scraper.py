import json
import csv
import requests
from functions import Greeting
from functions import RunProcess
from functions import SimpleCSV
from functions import Login

def main():
    pageUrl = []
    csvCategory = []
    idList = []
    idListCombine = []
    outputList = []
    remainRecords = 0

    Greeting.showInfo()
    logSession = Login.login()
    # get inputfile
    fileIn = SimpleCSV.getCSVInput()
    # get outputfile
    fileOut = SimpleCSV.getCSVOutput()
    pageUrl = SimpleCSV.readCSV(fileIn)
    numOfUrl = len(pageUrl)
    print("There are ", numOfUrl, " records in the input file.")
    # id scraping
    idListCombine = RunProcess.runProcess(pageUrl, idList, logSession)
    # write data to csv file
    print("Writing identifiers into ", fileOut, "...")
    outFile = open(fileOut, 'w', encoding = 'utf8', newline='')
    SimpleCSV.writeCSV(["internal id url"], outFile)
    SimpleCSV.writeCSVZipped(idListCombine, outFile)
    
    # program exit
    Greeting.sysExit(fileOut)
    
if __name__ == "__main__":
    main()
