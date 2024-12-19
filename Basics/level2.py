# # data type -2 type -mutable and immutable
# # mutable means change the state and content and immutable means object cannot

# # numberic -int,float,complex
# # sequence -string,list,tuple
# # dictonary
# # set



# # mutable data type -(list,dictionary,byte array)
# # imutable data type -(int,float,tuple,set,string,complex)


# # number
# a=5
# print(type(a))
# a=5.4
# print(type(a))
# a=5+4j
# print(type(a))

# # sequence

# # string
# s="Hello1@fnsfue"
# print(type(s))
# s=''' 
# Hello
#     welcome
# rni
# '''
# print(s)
# s='10'
# print(s)


# # list -ordered sequence of items -also mutable
# a=[1,4,2,'hi']
# a[2]="rni"
# print(a)

# tuple -ordered -more then 1 value compulsory
# a=(1,4,2,'hi')
# # a[2]="rni"
# print(a)
# a=(9)
# print(a,type(a))



# # dictionary =unordered collection of key value pairs and get value using key 
# d={1:"hi",'hlo':3,"name":"rni"}
# print(d["name"])
# print(d,type(d))

# # set -unirderd coollection of items - element should be unique ad immutable
# set_items={1,2,3,2,5}
# print(set_items,type(set_items))



# # getting user input and type casting

# a=input("enter the number1:-")
# b=input("enter the number2:-")
# print(a+b)

# a=int(input("enter the number1:-"))
# b=int(input("enter the number2:-"))
# print(a+b)

# # same for float but enter value with float 
# a=eval(input("enter the number1:-"))
# b=eval(input("enter the number2:-"))
# print(a+b)


# # conditional statement

# # if statement
# a=int(input("enter value1:-"))
# if a%2==0:
#     print(a,"Even number")
#     print(a,"Even number")   
# else: 
#     print("odd number")

# # if elif else

# a=90
# if(a>=90):print("A grade")
# elif (a>=60):print("B grade")
# else:print("pass")


# # build simple calculator
# a=int(input("enter value1:-"))
# b=int(input("enter value2:-"))
# opt=input("enter operator like +,-,*,/")

# if(opt=="+"):print(a+b)
# elif(opt=="-"):print(a-b)
# elif(opt=="*"):print(a*b)
# elif(opt=="/"):print(a/b)

# else:print("invalid operator")



# for loop with range()

# range(5)-0,1,2,3,4     type 1 end with default start with 0 and end with n-1
for i in range(5):
    print(i,"hi")

# range(1,5)- 1,2,3,4   type 2 start with and end with 
for i in range(1,5):
    print(i,"hi")
# range (1,10,2)  type 3 start and end with and 3rd is increment so 1,3,5,7,9
for i in range(1,10,2):    
    print(i,"hlo")    

# print(i)    

# # multiply table print
for i in range(1,11):
    print("2*",i ,"=",2*i)



# while loop

i=1
while i<=5:
    print(i)
    i=i+1 
    i+=1

