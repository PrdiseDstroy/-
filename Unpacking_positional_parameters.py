def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [12.23, 'Good', True]
values_dict = {'a': 2, 'b': 'Hey', 'c' : [1, 2 ,3]}
values_list_2 = ['str', (1, 2 ,3)]
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
