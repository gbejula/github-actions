mytuple = ("Dave", 34, False)

anothertuple = (1, 2, 4, 8, 4, 4)
print(mytuple)
print(type(mytuple))

newlist = list(mytuple)
newlist.append('Ibukun')
newtuple = tuple(newlist)

print(newlist)
print(newtuple)

print(anothertuple.count(4))