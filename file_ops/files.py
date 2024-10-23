import os
# r = read
# a = append
# w = write
# x = create

# Read = error if it doesn't exist

f = open("C:/Users/Gbenga/Documents/Gbenga/pyproject/file_ops/names.txt")
#print(f.read())
# print(f.read(5))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()


# Append - creates a file if it doesn't exist

f = open("C:/Users/Gbenga/Documents/Gbenga/pyproject/file_ops/names.txt", "a")
f.write("\nTokunbo")
f.close()

f = open("C:/Users/Gbenga/Documents/Gbenga/pyproject/file_ops/names.txt")
print(f.read())
f.close()

# Write (Overwrite)
f = open("C:/Users/Gbenga/Documents/Gbenga/pyproject/file_ops/context.txt", "w")
f.write("I deleted all file inside the context file")
f.close()

f = open("C:/Users/Gbenga/Documents/Gbenga/pyproject/file_ops/context.txt")
print(f.read())
f.close()

f = open("C:/Users/Gbenga/Documents/Gbenga/pyproject/file_ops/name_list.txt", "w")
f.close()

# Creates a file

# Creates the specified file, but returns an error if the file exists
if not os.path.exists("learn.txt"):
    f = open("learn.txt", "x")
    f.close()


# Delete a file

# avoid an error if doesn't exist
if os.path.exists("learn.txt"):
    os.remove('learn.txt')
else:
    print('The file you want to delete does not exist')


with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)