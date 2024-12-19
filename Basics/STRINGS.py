
# # string in py

# # it is a seq of char ,enclosed within single or double quotes 

# # welcome left to right read then 0 start and end side of read then start with -1 ,..
# # w="Welcome to my tutorial"

# # # indexing in string
# # print(w[6])  # get e 
# # print(w[-1])  # get l

# # print(w[0:9])  #slicing means get perticular data 
# # print(w[0:])
# # print(w[0:7:2])
# # print(w[0::2])

# # print(w[-1:-10:-2])
# # print(w[-1::-1])

# # string iteration

# w="welcome to my tutoriales"
# # l=len(w)
# # print(l)
# # for i in range(l):
# #     print(w[i])

# # # # lower ,upper,title,capitalize
# # print(w.lower())
# # print(w.upper())
# # print(w.title())  # word no fisrt char capital
# # print(w.capitalize())   #only 1st word char is a capital

# # # find ,index,isalpha,isdigit,isalnum

# # # find use for index of char and default start with 0  and also if char is not present then return -1

# print(w.find("w"))
# print(w.find("e",3))  
# print(w.find("we"))
# print(w.find("W"))

# # in index char is not present then display run time error
# print(w.index("w"))


# # # isalpha
# d="dnnnnnsjfff"
# e="dnnnnnsjfffddddss444"
# el="dnnnnnsjfffdd ddss444"
# f="777"
# print(d.isalpha())
# print(e.isalpha())
# print(e.isdigit())
# print(f.isdigit())
# print(e.isalnum())
# print(el.isalnum())
 


# # # chr and ord

# # # chr -?used for pass arg as a int and return a asci value char string
# w=chr(65)
# print(type(w),w)

# # ord ->pass char as a parameter and return integer asci value
# y=ord("H")
# print(type(y),y)


# # # string format () method  -> used for placeholder  -also called as a run time evalution

# # naming placeholder
# txt1="Welllcome {name} how are you {surname}".format(name="rni" , surname="varsanni")
# # numbered placeholder
# txt2="Welllcome {0} {1}".format("rni" ,"varsanni")
# txt3="Welllcome {1} {0}".format("rni" ,"varsanni")
# # empty placeholder
# txt4="Welllcome {} {} {}".format("rni" , "varsanni","")

# w="Welcome {b:>10} to {a}".format(a=30,b=40)  # >means char goto right side and <means go to left side and ^ means center and around space
# print(txt1)
# print(txt2)
# print(txt3)
# print(txt4)
# print(w)

# w1 = "Welcome {b:>10} to {a}".format(a=30, b=40)  # Right-aligned (width 10)
# w2 = "Welcome {b:<10} to {a}".format(a=30, b=40)  # Left-aligned (width 10)
# w3 = "Welcome {b:^10} to {a}".format(a=30, b=40)  # Center-aligned (width 10)
# w4 = "Welcome {b:_^10} to {a}".format(a=30, b=40) # Center-aligned with '_' padding

# print(w1)
# print(w2)
# print(w3)
# print(w4)





# string is a colllection of char and enclsed within a "",'',''' '''

s1="Hello, Worlf"
s2='Hello, Worlf'
s3='''Hello, Worlf
        twinkle twinkle little 
        star !'''

print(s1,s2,s3)


# indexing :py support positive and  negative indexing       if you start from left then 0 to ... and if you start from right to left then -1 ,..
s="Python"
print(s[0]) # P
print(s[-1]) # n


# slicing means extract a portion of the string  ------  syntax :[start:stop:steps]  ____

s="Pythonisaprogramminglanguage"
print(s[5])
print(s[2:9])
print(s[1:])
print(s[:10])
print(s[0::2])
print(s[-1::-4])

# build in methods 
    #     upper()	Converts all characters to uppercase.
    # lower()	Converts all characters to lowercase.
    # capitalize()	Capitalizes first letter of string.
    # title()	Capitalizes first letter of each word.
    # swapcase()	Swaps case of each character.
s="hello WRLD fffffEw"    
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())



# string validation 
    #     isalpha()	Checks if all characters are letters.
    # isdigit()	Checks if all characters are digits.
    # isalnum()	Checks if all characters are letters/digits.
    # isspace()	Checks if string contains whitespace only.
    # isupper()	Checks if all characters are uppercase.
    # islower()	Checks if all characters are lowercase.

s="Python123"
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.isspace())
print(s.isupper())
print(s.islower())


# search and replce


    # find(substring)	Returns index of first occurrence, -1 if not found.
    # index(substring)	Returns index of first occurrence, error if not found.
    # replace(old, new)	Replaces all occurrences of old with new.
    # count(substring)	Returns number of times a substring appears.

s="hellow world, helloe Python"    

print(s.find("hellow"))
print(s.find("hello",7))
print(s.find("H"))
print(s.index("hello"))
# print(s.index("H"))
print(s.replace("h","m"))
print(s.count("o"))


# spliting and joining

    # split()	Splits string into a list (default: space).
    # splitlines()	Splits string into lines (for multiline).
    # join(iterable)	Joins elements of a list/tuple into a string.

s="python is fun"

# spliting
print(s.split())
# splitlines
print(s.splitlines())
# Join a list of strings with ","
print(",".join(["a", "b", "c"]))  # Output: 'a,b,c'

# Join characters in a string
print(",".join(s))  # Output: 'p,y,t,h,o,n, ,i,s, ,f,u,n'


# trimming and whitespace

    # strip()	Removes leading and trailing whitespaces.
    # lstrip()	Removes leading whitespaces.
    # rstrip()	Removes trailing whitespaces.

s="    Hi, Python   "    
print(s.strip())
print(s.lstrip())
print(s.rstrip())