import stable_matching_helpers as helpers

temp = dict
helpers.inverse_dict(temp)


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
        matchedList.append(helpers.matching_from_lists(x[0], x[1])
    return matchedList


#
