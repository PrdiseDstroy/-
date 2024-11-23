calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(a):
    count_calls()
    global calls
    b = (len(a), a.upper(), a.lower())
    return b
def is_contains(string, list_to_search ):
    count_calls()
    a = string.lower() in list_to_search
    return a

print(string_info('Hello'))
print(is_contains('one'.lower(), ['one', 'two', 'three']))
print((is_contains('apple', ['one', 'two', 'three'])))
print(calls)