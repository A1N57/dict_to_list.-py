def filter_list(my_list, type1):
    return list(filter(lambda elem: type(elem) is type1, my_list))

print(filter_list([1, True, 'as', 5], int))
