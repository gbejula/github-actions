squared = lambda num: num * num
print(squared(2))

addTwo = lambda num: num + 2
print(addTwo(15))

sum_total = lambda a,b: a + b

print(sum_total (2, 3))


####################################

def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

################################333

# Higher order function.

# map

nums = [4, 5, 7, 9, 13, 15, 20]

squared_nums = map(lambda num: num * num, nums)

print(list(squared_nums))

################################

# filter

odd_nums = filter(lambda num: num % 2 != 0, nums)

print(list(odd_nums))

################################

from functools import reduce

numba = [1, 2, 3, 4, 5, 2]

total = reduce(lambda acc, curr: acc + curr, numba, 10)

print(total)

print(sum(numba, 10))

names = ['Olugbenga Ajayi', 'Adedayo Adeyomoye', 'Samson Adegunle', 'Israel Adeyemi', 'Babatunde Moruf']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)