import stable_matching_helpers as helpers
import ast
import json
import sys


    # freeMen should be the list of men free, which each have a list of free women
def gale_shapely():

    while has_free(freeMenList) and has_proposals(freeMenList, menDict):

        # if the woman of the first free man is free
        # print(menDict.get(freeMenList[0]))
        if isFree(menDict.get(freeMenList[0])[0], freeWomenList):
            #print(menDict.get(freeMenList[0])[0])
            join(freeMenList[0], menDict.get(freeMenList[0])[0])

        else:
            #print(menDict.get(freeMenList[0])[0])
            if prefers_Current(menDict.get(freeMenList[0])[0], freeMenList[0]):
                #print(menDict[freeMenList[0]])
                menDict[freeMenList[0]].remove(menDict.get(freeMenList[0])[0])
                #print(menDict[freeMenList[0]])

            else:
                end_Marriage(freeMenList[0], menDict.get(freeMenList[0])[0])
                join(freeMenList[0], menDict.get(freeMenList[0])[0])



    #puts men and woman back in free
def end_Marriage(man, woman):
    if galeDict.get(man) is not None:
        galeDict.pop(man)
    freeMenList.append(man)
    freeWomenList.append(woman)


    # combines man and woman, and removes from free lists
def join(man, woman):

    menDict[man].remove(woman)

    galeDict.update({man: woman})



    freeMenList.remove(man)
    freeWomenList.remove(woman)



def prefers_Current(woman, man):
    if not list(menDict.values()).__contains__(woman):
        return False
    
    else:
        for key, value in galeDict.iteritems():
            if value == woman:
                man2 = galeDict[key]


        if womenDict.get(woman).index(man) < womenDict.get(woman).index(man2):
            return True
        return False


    #freemen list isn't null
def has_free(menL):
    if len(menL) > 0:
        return True
    return False


def isFree(woman,womenL):
    if woman in womenL:
        return True
    return False


def has_proposals(menL, menDict):
    for x in range(len(menL)):
        if len(menDict.get(menL[x])) > 0:
            return True
    return False


def write_json(obj, filename):
    with open(filename, mode='w') as f:
        json.dump(obj, f) 

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:
        data = ast.literal_eval(f.read())

    finalList = []

    for x in range(len(data)):
        menDict = data[x][0]
        womenDict = data[x][1]

        freeMenList = list(dict.keys(menDict))
        freeWomenList = list(dict.keys(womenDict))

        galeDict = {}
        gale_shapely()

        finalList.append(galeDict)
        write_json(finalList,sys.argv[2])
    





