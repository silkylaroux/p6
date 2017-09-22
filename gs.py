if __name__ == '__main__':
    import stable_matching_helpers as helpers
    import ast
    import json
    import sys
    import defaultdict

    with open (sys.arg[1],'r') as f:
        data = ast.literal_eval(sys.arg[1],'r')
    helpers.inverse_dict(data)

    freeMen = [dict() for x in range(data)]
    d = defaultdict(list)
    
    # freeMen should be the list of men free, which each have a list of free women 
    def gale_shapely():
        while has_free() and not has_proposals():

            #if the woman of the first free man is free
            if isFree(freeMen[0][0]):
                join(freeMen[0],freeMen[0][0])
            else:
                if prefers(freeMen[0][0]):
                    pass

    def join( m, w):
        pass
    
    def has_free():
        pass


    def isFree():
        pass


    def has_proposals():
        pass


    # checks if list is empty
    def is_Empty(l):
        if (len(l) == 0):
            return False
        return True


    # breaks full list into pairings of dictionaries
    def break_dict_List(l):
        listDictHolder = list()
        for x in l:

            tempList = [helpers.dict_to_pref_list(
                x[0]), helpers.dict_to_pref_list(x[1])]

            listDictHolder.append(tempList)
        return listDictHolder


    # goes through list of lists and makes matches
    def match_maker(l):
        matchedList = list()
        for x in l:
            matchedList.append(helpers.matching_from_lists(x[0], x[1]))
        return matchedList
