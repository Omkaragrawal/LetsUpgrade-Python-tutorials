List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

Set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

Dictionary = {'a': 1, "b": 2}

def doubler(number):
    return number * 2


list_of_list = list(map(doubler, List))
print(list_of_list)


set_of_tuple = set(map(lambda x: x*2, Tuple))
print(set_of_tuple)


set_of_set = set(map(lambda x: x*2, Set))
print(set_of_set)


list_of_dictionary = list(map(lambda x: Dictionary.get(x) * 2, Dictionary))
print(list_of_dictionary)

print(list(map(lambda x, y, z: x + y + z, List, Tuple, Set)))