# функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(2, )
print_params(2, 3)
print_params('str', 5, False)

# распаковка элементов

values_list = [5, 'int', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

# распаковка + отдельные элементы

values_list2 = (54.32, 'Строка')
print_params(*values_list2, 42)