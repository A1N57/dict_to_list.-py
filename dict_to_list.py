def dict_to_list(a):
    list = []
    for k, v in a.items():
      if type(v) == int:
        v *= 2
        list.append((k, v))    
    return list
print(dict_to_list({'f': 2, 'r': 3}))
