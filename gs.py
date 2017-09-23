if __name__ == '__main__':
    import stable_matching_helpers as helpers
    import ast
    import json
    import sys
    import defaultdict

    with open (sys.arg[1],'r') as f:
        data = ast.literal_eval(f.read())

    for x in data:
        menDict = data[x][0]
        womenDict = data[x][1]
        
        freeMenList = dict.keys(menDict)
        freeWomenList = dict.keys(womenDict)

        gale_shapely(freeMenList,women,menDict,womenDict)



    # freeMen should be the list of men free, which each have a list of free women 
    def gale_shapely(menL,womenL,menD,womenD):
        while has_free(menL) and not has_proposals(menL):

            #if the woman of the first free man is free
            if isFree(menD.get(menL[0])[0]):
                join(menL[0],freeMen[0][0])
            else:
                if prefersCurrent(freeMen[0][0],freeMen[0]):
                    pass
                else:
                    endMarriage(freeMen[0][0])
                    join(freeMen[0][0])


    #puts men and woman back in free
    def end_Marriage(w):
        pass

    # combines man and woman, and removes from free lists
    def join(m, w):
        pass


    def prefers_Current(w, m):
        pass


    #freemen list isn't null
    def has_free(m):
        if m is None:
            return False
        return True

    def isFree(w):
        pass


    def has_proposals():
        pass


