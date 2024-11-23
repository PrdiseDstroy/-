calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    global calls
    b = (len(string), string.upper(), string.lower())
    return b
def is_contains(string, list_to_search ):
    count_calls()
    a = string.lower() in list_to_search
    return a

print(string_info('Hello'))
print(is_contains('one'.lower(), ['one', 'two', 'three']))
print((is_contains('apple', ['one', 'two', 'three'])))
print(calls)
