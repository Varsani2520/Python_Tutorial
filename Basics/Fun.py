def great():
    print("hellow world")


# call the function
great()


# func with args
def greet(name):
    print(f"hi {name}")

greet("varsani")    

# func with arg and return type

def add(a,b):
    return a+b

result=add(3,4)
print(result)


# func with type annotations(indicate expected arg and return type)

def multiply(a:int,b:int)->int:
    return a*b
result=multiply(4,5)
print(result)


# function with default arguments
def greets(name="guest"):
    print(f"hi,{name}")

greets("rahul")    
greets()
