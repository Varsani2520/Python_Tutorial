l = [10, 20, 10, "hi"]  # List with multiple data types
print(l)

# list iteration
for i in l:
    print(i)


l = [10, 20, 30, 40,10,30]

# Pop method
l.pop(2)  # Removes item at index 2
print("After pop:", l)

# Remove method
l.remove(10)  # Removes first occurrence of 10
print("After remove:", l)

# Clear method
l.clear()  # Removes all elements
print("After clear:", l)


l = [10, 20, 10, 30, 40]

# Count method
print("Count of 10:", l.count(10))

# Max and Min
print("Max:", max(l))
print("Min:", min(l))

# Sort method
l.sort()
print("Sorted list:", l)

# Reverse method
l.reverse()
print("Reversed list:", l)

# Index method
print("Index of 30:", l.index(30))


# The zip() function allows you to combine multiple lists and iterate over them simultaneously.

l1=[10,20,30]
l2=["navin","mann","nayan"]

print(list(zip(l1,l2)))
# iteration
for a,b in zip(l1,l2):
    print(a,b)
# other way
for a,b in zip(l1,l2):
    print(f"{b} scored in exams is {a}")

# unzip
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*zipped)

print(list1)  # Output: (1, 2, 3)
print(list2)  # Output: ('a', 'b', 'c')

# combining and sum list
list1 = [1, 2, 3]
list2 = [4, 5, 6]

summed = [a + b for a, b in zip(list1, list2)]
print(summed)  # Output: [5, 7, 9]


# string to list conversion
s="Hellow are you"
print(s.split()) 

# split with specify
s="apple,mango,banan"
print(s.split(","))

# Splits the string into a list of lines.


string = "hello\nworld\npython"
line_list = string.splitlines()
print(line_list)


string = "12345"
num_list = [int(char) for char in string]
print(num_list)


# implementing stack and queue using ist daa type

# stack is fifo or lifo and 
# 4 operaton : 1->push()-insert value
# 2->pop()->remove top most element
#3:peek()->display top most element
#4->display->display list


l=[]
while True:
    c=int(input('''
    1 push operation
    2 pop operation
    3 peek element
    4 display stack
    5 exit
    '''))
    if(c==1):
        n=input("enter value")
        l.append(n)
        print(l)
    elif(c==2):
        if len(l)==0:print("stack is empty")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif(c==3):
        if len(l)==0:print("empty stack")
        else: print("laststack value",l[-1])
    elif(c==4):
        print("display stack",l)  

    elif c==5:break;
          


