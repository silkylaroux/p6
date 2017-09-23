if __name__ == '__main__':
    import stable_matching_helpers as helpers
    import ast
    import json
    import sys
    import defaultdict

    with open (sys.arg[1],'r') as f:
        data = ast.literal_eval(f.read())

    finalList = []

    for x in data:
        menDict = data[x][0]
        womenDict = data[x][1]
        
        freeMenList = dict.keys(menDict)
        freeWomenList = dict.keys(womenDict)

        galeDict = {}
        gale_shapely(freeMenList,freeWomenList,menDict,womenDict,galeDict)



    # freeMen should be the list of men free, which each have a list of free women
    def gale_shapely(menL,womenL,menD, womenD, dictionary):
        while has_free(menL) and not has_proposals(menL):

            #if the woman of the first free man is free
            if isFree(menD.get(menL[0])[0],womenL):

                join(menL[0],menD.get(menL[0])[0])

            else:
                if prefersCurrent(freeMen[0][0],freeMen[0]):
                    pass
                else:
                    endMarriage(freeMen[0][0])
                    join(freeMen[0][0])


    #puts men and woman back in free
    def end_Marriage(man, woman, menL, womenL):


    # combines man and woman, and removes from free lists
    def join(menL, womenL):
        pass


    def prefers_Current(woman, man, womenL):
        pass


    #freemen list isn't null
    def has_free(menL):
        if menL is None:
            return False
        return True


    def isFree(woman,womenL):
        if woman in womenL:
            return True
        return False


    def has_proposals(menL, menDict):
        for x in menL:
            if menDict.get(menL[x]) is None:
                return False
        return True


