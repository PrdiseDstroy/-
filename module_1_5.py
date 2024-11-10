immutable_va= (1, 'a', True)
print(immutable_va)
immutable_va= (1, 'a', True)
immutable_va[0]= 2
print(immutable_va) # Ошибка возникает из-за того, что картеж является неизменяемым объектом
mutable_list=['apple','banana', 'watermelon']
mutable_list[2]='pear'
print(mutable_list)