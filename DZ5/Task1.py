def get_even():
    for i in range (1,15):
        if i % 2 != 0:
            yield i
a = get_even()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))