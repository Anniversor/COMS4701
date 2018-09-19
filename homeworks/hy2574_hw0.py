"""
COMS W4701 Artificial Intelligence - Homework 0

In this assignment you will implement a few simple functions reviewing
basic Python operations and data structures.

@author: YOUR NAME (YOUR UNI)
"""


def manip_list(list1, list2):
    # YOUR CODE HERE
    print(list1[-1])
    list1.pop()
    list2[1] = list1[0]
    print(list1+list2)

    return [list1, list2] # replace this


def manip_tuple(obj1, obj2):
    # YOUR CODE HERE
    new_tuple  = (obj1, obj2)
    new_tuple[0] = obj2
    return None


def manip_set(list1, list2, obj):
    # YOUR CODE HERE
    set1 = set(list1)
    set2 = set(list2)
    set1.add(obj)
    print(obj in set2)
    print(set1-set2)
    print(set1|set2)
    print(set1&set2)
    set1.remove(obj)

    return None


def manip_dict(tuple1, tuple2, obj):
    # YOUR CODE HERE
    dictionary = dict(zip(tuple1, tuple2))
    print(dictionary[obj])
    dictionary.pop(obj)
    print(len(dictionary))
    dictionary[obj] = 0
    return [(k,v) for k,v in dictionary.items()]

if __name__ == "__main__":
    #Test case
    print(manip_list(["artificial", "intelligence", "rocks"], [4701, "is", "fun"]))

    try: manip_tuple("oh", "no")
    except TypeError: print("Can't modify a tuple!")

    manip_set(["sets", "have", "no", "duplicates"], ["sets", "operations", "are", "useful"], "yeah!")

    print(manip_dict(("list", "tuple", "set"), ("ordered, mutable", "ordered, immutable", "non-ordered, mutable"), "tuple"))