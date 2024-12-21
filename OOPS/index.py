#1. class is a blueprint for creating a object and obj is a instance of class

# class
class Person:
    a=10
    
    def greet(self):
        print("Hello welcome")
    def show(self):
        self.c=self.a*self.a
        print(self.c)
    def sum(self,a,b):
        print(a+b)
            



# obj
p=Person()
p.greet()
p.show()
p.sum(3,4)












# constructor
class student:
    def __init__(self):
        self.__name=""
    #get method
    def getName(self):
        return self.__name 
    #set method
    def SetName(self,name):
         self.__name=name 


obj=student()
obj.SetName("Testing")
r=obj.getName()
print(r)

# inheritance ->allow 1 class to derive the properties and method of another class

# Single inheritance
class A:
    def method_a(self):
        print("Method A is executed.")

class B(A):  # B inherits from A
    def method_b(self):
        print("Method B is executed.")

# Multi-level inheritance
class C(B):  # C inherits from B, which inherits from A
    def method_c(self):
        print("Method C is executed.")
# Testing Single and Multi-level Inheritance
print("Single and Multi-level Inheritance:")
obj_c = C()
obj_c.method_a()  # From A
obj_c.method_b()  # From B
obj_c.method_c()  # From C


# Multiple inheritance
class Animal1:
    def dog1(self):
        print("dog1")
class Animal2:
    def dog2(self):
        print("dog2")
class Animal3(Animal1,Animal2):
    def dog3(self):
        print("dog3")

# Testing Multiple Inheritance
print("\nMultiple Inheritance:")
obj_d = Animal3()
obj_d.dog1()  # From 1
obj_d.dog2()  # From 2
obj_d.dog3()  # From 3




#  Encapsulation restricts direct access to an object’s data and methods and can be achieved using private members (__).

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # Error: AttributeError
 
 
 
#  polymorphism
# Polymorphism allows the same method to behave differently depending on the object.

class Bird:
    def fly(self):
        print("Bird can fly")
    def fly(self):
        print("Bird can fly1")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")
bird=Bird()
penguin = Penguin()

bird.fly()      # Output: Bird can fly
penguin.fly()   # Output: Penguin cannot fly
