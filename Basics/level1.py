print("hellow",'hello','''hi''',10)
# return true or false
print(10>7) 



# var doesnot start with digit 
# 1a=20
# in python location based on value not a variable
a=10
b=10
print(a,b)
# location of a and b  
print(id(a),id(b))  
# same location for a and b take a garbadge value


# var dosent contain space 
# a b=10
a_b=10



# string 
name="varsani"
surname="hi"
# concate (str to str)
print(name+" "+surname)  
c=20
print(c+20)
# print(name+c)


# operator

# arithmethic (+,-,*,/,%,**,//)
num1=20
num2=5
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)
# float divison if 3.333 to return only 3 inshort int 
print(num1//num2)  


# assignment (=,+=,-=)
x=3
print(x)
# increment with 5
x=x+5 
print(x)
x+=5 
print(x)
# decremrnt
x=x-5 
print(x)
x-=5 
print(x)

# comparison operator(<,>,<=,>=,==,!=) that return only true and false
print (num1==num2)

# logical operatior (and ,or,not)

p=10
q=20
print(p==10 and p<q)
print(p==20 or p<q)
# reverse of p 
print( not p!=10)



# memershop (element is present in the list)
String1="Helloe"
print('h'in String1)
print('H'in String1)

l=[10,20,30]
print(50 in l)
print(50 not in l)

# identity operator(is or is not)
print(p is q,p==q)
print(p is not q,p!=q)


# bitwise operator(&-and,|-or ,^-xor)
# in xor both same then 0 otherwise 1 
x=10
y=8
print(bin(x))
print(bin(y))
print(x&y ,bin(x&y))
