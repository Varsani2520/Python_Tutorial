# tuple is immutable and orderd and hold mix data type ,similer like list but not change a value and also ordered

#1 create a tupel
t=(3,4,"name")
print(t)
# tuple with 1 elemnt(add trailing comma)
single_tuple=(3,)
# single_tuple=(3,)
print(type(single_tuple),single_tuple)
# Empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)  # Output: ()


#2.acess elem

t = (1, 2, 3, "Rahul", True)

# Access by index
print(t[0])  # Output: 1
print(t[3])  # Output: 'Rahul'

# Negative indexing
print(t[-1])  # Output: True
print(t[-3])  # Output: 3


t = (1, 2, 3, 4, 5)

#3 Slice from index 1 to 3 (excluding 3)
print(t[1:3])  # Output: (2, 3)

# Slice from start to index 3
print(t[:3])  # Output: (1, 2, 3)

# Slice from index 2 to end
print(t[2:])  # Output: (3, 4, 5)

# Step slicing
print(t[::2])  # Output: (1, 3, 5)


# 4. Tuple Operations
# a) Concatenation
# You can combine two tuples using the + operator.

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4, 5, 6)
# b) Repetition
# You can repeat a tuple using the * operator.


t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)
# c) Membership
# You can check if an element exists in a tuple.


t = (1, 2, 3)
print(2 in t)   # Output: True
print(5 in t)   # Output: False
# d) Length
# You can find the length of a tuple using len().

t = (1, 2, 3)
print(len(t))  # Output: 3


# 5.methods 

# count
t=(1,3,4,2,4,4,6,4)
print(t.count(4))

# index
print(t.index(3))  #index of 3 =2

#6.packing and unpacking
packed_tuple=1,2,"rahul"
print(packed_tuple)

t=(1,4,"roman")
a,b,c=t
print(a)
for i in t:
    print(i)



#7.nesting tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])  # Output: (1, 2)
print(nested_tuple[0][1])  # Output: 2