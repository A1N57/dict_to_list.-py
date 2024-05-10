def filter_list(my_list, type1):
    def check_element(elem):
        return isinstance(elem, type1)
    return list(filter(check_element, my_list))

print(filter_list([1, True, 'as', 5], int))
