def helloWorld():
    print('Hello World!')

helloWorld()

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum(5, 9)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("David", "Ibukunoluwa", "Jesutoba")

def multNamedItems(**kwargs):
    print(kwargs)
    print(type(kwargs))

multNamedItems(first="Ibukunoluwa", middle="Ruth", last="Ajayi")