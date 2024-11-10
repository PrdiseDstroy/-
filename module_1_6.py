my_dict={'Pavel': 1999}
my_dict['Ira']= 2000
my_dict.update({'Denis': 1980 ,
               'Inga': 2002})
del my_dict['Ira']
print(my_dict)

my_set= {1, False, 'a', True, 1, 'a', True, 1, 'a', False }
my_set.update({'man',
               'woman'})
my_set.discard('man')
print(my_set)
