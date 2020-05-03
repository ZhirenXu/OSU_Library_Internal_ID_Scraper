##Put group of ID together
# @param    iter0
#           an iterator
# @param    iter1
#           an iterator
# @param    idList
#           a list contain id
# @param    idListCombine
#           a list contain list of id
# @return idListCombine
def createIDList(iter0, iter1, idList, idListCombine):
    print("Create identifier links...", end = "")
    httpSuffix = "https://library.osu.edu/dc/concern/generic_works/"
    while iter1 < len(idList):
        newID = httpSuffix + idList[0]
        idList.append(newID)
        idList.pop(0)
        iter1 += 1
    iter1 = 0
    print("OK")
    
    idListCombine.append(idList)
    return idListCombine
