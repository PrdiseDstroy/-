def test_function(a):
    def inner_function(a):
        return print('Я в области видимости функции test_function')
    inner_function(a)
test_function('')
