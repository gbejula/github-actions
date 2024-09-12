first = "Dave"



title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")
print("")

# string index values

print(first[1])
print(first[-1])
print(first[1:])
print("")

# Some methods return boolean type
print(first.startswith("D"))
print(first.endswith("E"))
print("")
#Numeric data types

# Integer type

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
print("")

# floating
gpa = 4.15

print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))
