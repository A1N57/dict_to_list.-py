def filter_list(my_list, type1):
    new_list = []
    for el in my_list:
        if type(el) == type1:
            new_list.append(el)
    return(new_list)

print(filter_list([1, True, 'as', 5], int))
