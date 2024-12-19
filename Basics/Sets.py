# Create a set (unordered, unindexed, no duplicates, mutable)
s = {1, 2, 3, 4, 5, "hi"}
print("Set s:", s)

# Iterate through the set (order is not guaranteed)
for a in s:
    print(a)

# Set function examples:
# 1. Using set() to convert a list to a set
l = [10, 20, "hi"]
print("Converted set:", set(l))  # Output: {10, 20, 'hi'}

# 2. remove() - Removes an element from the set, raises an error if not found
# Note: remove() method works on sets, not lists
s = {10, 20, 30}
s.remove(20)  # 20 is present, so it will be removed
print("After remove(20):", s)  # Output: {10, 30}

# 3. discard() - Removes an element if present, does nothing if not found
s.discard(50)  # 50 is not in the set, but no error will occur
print("After discard(50):", s)  # Output: {10, 30}

# 4. pop() - Removes and returns an arbitrary element from the set
popped_element = s.pop()
print(f"Popped element: {popped_element}")
print("After pop:", s)

# 5. clear() - Clears all elements from the set
s.clear()
print("After clear:", s)  # Output: set()

# 6. add() - Adds a single element to the set
s = {1, 2, 3}
s.add(70)
print("After add(70):", s)  # Output: {1, 2, 3, 70}

# 7. update() - Adds multiple elements (or another set, list, or tuple) to the set
l = [10, 20, 80, 90]
s.update(l)  # Add elements of the list l to the set s
print("After update:", s)  # Output: {1, 2, 3, 70, 10, 80, 90, 20}
