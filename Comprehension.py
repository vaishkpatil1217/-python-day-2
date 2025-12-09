list1 = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
print("original list:",list1)

no_list = [item for item in list1 if isinstance(item, (int, float))]
print("numeric list",no_list)
