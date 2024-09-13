users = ['Titi', 'Bayo', 'Dele']

print(users.index('Bayo'))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(users))

users.append("Bisi")
print(users)

users += ["Jibola"]
print(users)

users.extend(["Kola", "Folu"])
print(users)

users.sort()
print(users)

nums = [5, 1, 14, 72, 4]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)