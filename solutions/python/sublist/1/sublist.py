SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL


def is_sublist(smaller, bigger):
    if smaller == []:
        return True
    for i in range(len(bigger) - len(smaller) + 1):
        if bigger[i:i+len(smaller)] == smaller:
            return True
    return False
