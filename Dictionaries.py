# Dictionaries.

## They are used to store date values that are in key value pairs.

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

print(type(band))
print(len(band))

# Access items
print(band.get("guitar"))
print(band["vocals"])

# list all key
print(band.keys())

# list all values
print(band2.values())

print(band.items())

print("vocals" in band)
print("violin" in band2)

# Change values
band["vocals"] = "Keyboard"
band.update({"bass": "Coverdale"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # tuple
print(band)

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries
# bad copy
#band2 = band
#print(band)
#print(band2)

band2 = band.copy()
band2["drums"] = "Wale"
print("Good copy")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)  # good copy
print(band3)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band["member2"]["instrument"])


# SETS

nums = {1, 2, 3, 4}
nums2 = set((5, 4, 3, 2, 1))

print(nums)
print(nums2)
print(type(nums2))
print(len(nums))

# No duplicate allowed 
nums = {1, 2, 3, 3, 3}
print(nums)
print(len(nums))

# True is a duplicate of 1, False is a duplicate of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)
print(len(nums))

# check if a value is in a set
print(2 in nums)

# You cannot refer to an element in the set with an index position or key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# You can use update with lists, tuples, and dictionaries too.

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)