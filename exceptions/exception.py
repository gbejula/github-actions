x = 2
try:
    print(x/0)
except NameError:
    print('NameError means something is undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error:
    print(error)
else:
    print('No errors')
finally:
    print('This will print with or without an error.')