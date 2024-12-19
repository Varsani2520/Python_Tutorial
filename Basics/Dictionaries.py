# Denoted by {} and it is a key-value pair

# 1. Create a dictionary
d = {"name": "rahul", "ice--cream": 10}
print("Original Dictionary:", d)  # Output: {'name': 'rahul', 'ice--cream': 10}

# 2. Access a value using a key
print("Value of 'name':", d["name"])  # Output: rahul

# 3. Iterate through the dictionary
print("Iterating through the dictionary:")
for key in d:
    print(f"Key: {key}, Value: {d[key]}")  # Output: rahul, 10

# 4. Using get()
print("Using get() method:")
print(d.get("name"))  # Output: rahul
print(d.get("age", "Key not found"))  # Output: Key not found

# 5. keys()
# Returns a view object of all the keys in the dictionary.
print("Keys:", d.keys())  # Output: dict_keys(['name', 'ice--cream'])

# 6. values()
# Returns a view object of all the values in the dictionary.
print("Values:", d.values())  # Output: dict_values(['rahul', 10])

# 7. items()
# Returns a view object of all key-value pairs as tuples.
print("Items:")
for k, v in d.items():
    print(f"Key: {k}, Value: {v}")
    # Output:
    # Key: name, Value: rahul
    # Key: ice--cream, Value: 10

# 8. Add a new key-value pair
d["age"] = 25
print("After Adding 'age':", d)  # Output: {'name': 'rahul', 'ice--cream': 10, 'age': 25}

# 9. Update a value
d["name"] = "Rahul Sharma"
print("After Updating 'name':", d)  # Output: {'name': 'Rahul Sharma', 'ice--cream': 10, 'age': 25}

# 10. Update using update()
d.update({"city": "Mumbai", "country": "India"})
print("After Update Method:", d)
# Output: {'name': 'Rahul Sharma', 'ice--cream': 10, 'age': 25, 'city': 'Mumbai', 'country': 'India'}

# 11. Delete a key-value pair using del
del d["ice--cream"]
print("After Deleting 'ice--cream':", d)  # Output: {'name': 'Rahul Sharma', 'age': 25, 'city': 'Mumbai', 'country': 'India'}

# 12. Delete a key-value pair using pop()
popped_value = d.pop("age")
print("Popped Value of 'age':", popped_value)  # Output: 25
print("After Popping 'age':", d)  # Output: {'name': 'Rahul Sharma', 'city': 'Mumbai', 'country': 'India'}

d = {"name": "rahul", "age": 25, "city": "Mumbai"}

# Using del
del d["age"]
print(d)  # Output: {'name': 'rahul', 'city': 'Mumbai'}

# Using pop
city = d.pop("city")
print(city)  # Output: 'Mumbai'
print(d)  # Output: {'name': 'rahul'}


# 13. Clear the dictionary
d.clear()
print("After Clearing Dictionary:", d)  # Output: {}

# 14. Create a dictionary using dict()
new_dict = dict(a=1, b=2, c=3)
print("New Dictionary:", new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 15. From an iterable of pairs
pairs = [("x", 10), ("y", 20), ("z", 30)]
another_dict = dict(pairs)
print("Another Dictionary from Pairs:", another_dict)  # Output: {'x': 10, 'y': 20, 'z': 30}

# 16. Check if a key exists
print("Is 'x' in another_dict?", "x" in another_dict)  # Output: True
print("Is 'a' in another_dict?", "a" in another_dict)  # Output: False

# 17. Get the length of the dictionary
print("Length of another_dict:", len(another_dict))  # Output: 3



# nested dict
# Nested dictionary example
nested_dict = {
    "person1": {
        "name": "Rahul",
        "age": 25,
        "city": "Mumbai"
    },
    "person2": {
        "name": "Anjali",
        "age": 30,
        "city": "Delhi"
    },
    "person3": {
        "name": "Karan",
        "age": 28,
        "city": "Bangalore"
    }
}

print("Nested Dictionary:", nested_dict)

# acessing element
print(nested_dict["person1"]["name"])
print(nested_dict["person1"]["city"])

# addeing items
nested_dict["person4"]={"name":"simran","age":34}
print(nested_dict)

# add in inner key
nested_dict["person1"]["proffesion"]="Engineer"
print(nested_dict)

# modufy
nested_dict["person2"]["age"]=45
print(nested_dict)

# delete
del nested_dict["person1"]["city"]
print(nested_dict)