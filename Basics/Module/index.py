# # call method 1
# import Functions

# print(Functions.sum(8,9))
   
# # call method 2-only call that fun or specific items
# from Functions import multiply
# print(multiply(8,9))

# from Functions import *
# print(multiply(8,9))


# # method 3 using alias
# import Functions as f

# print(f.sum(8,9))




# # Math Module in Python
# import math
# # 1.ceil()->return only integeger value
# x=10.6
# print("ceil:",math.ceil(x))
# print("floor:",math.floor(x)) 

# # 2.fabs-return positive number
# y=-12
# print(math.fabs(y))

# # 3.factorial
# print(math.factorial(5))

# #4.FSUM
# l=[1,4,6,3]
# # l=[1,4,6,3.0]
# print("return sum:",math.fsum(l))

# # sqrt=>squart root
# print(math.sqrt(4))

# print(math.pi)
# print(math.e)





# # python random module
# import random

# # randint() ->it return  number between 1(included) to 10 (not included)
# print(random.randint(1,10))

# # chice=>return random element from the list
# l=["banana","cherry","apple","grapes","mango"]
# print("random list:",random.choice(l))

# # random ->return value between 0 to 1
# print("random value generated",random.random())

# # shuffle ->change arrangements
# l=[10,20,30,50]
# random.shuffle(l)
# print(l)

# # uniform ->return value between range but in formof float
# u=random.uniform(3,9)
# print(u)




# # python datetime
# # as a object

# import datetime as d

# print(d.datetime.now()) # current time -year month-date-hour-minute-second-milisecond

# print(d.datetime(2022,3,3))


# # strtime shortcut of datetime
# # %b=short name of month dec,,, ___
# # %B= full month name like december _
# # %m=month as a number like 12  ____
# # %y=year,short version,without century like 18 _________
# # %Y =year like 2018     _________ 
# # %H ex 17 full hr   _________
# # %l->return according to 12 hr     ____________ 
# # %p=am/pm   _______
# # %M=minute 
# x=d.datetime.now()
# month=x.strftime("%Y")  # specific year
# print(month)
# month=x.strftime("%y")  # specific year short term
# print(month)
# month=x.strftime("%b")  # specific month but in short
# print(month)
# month=x.strftime("%B")  # specific month but in short
# print(month)
# month=x.strftime("%M")  # return minute
# print(month)
# month=x.strftime("%m")  # return month
# print(month)
# month=x.strftime("%p")  # return AM/pm
# print(month)
# month=x.strftime("%H")  # return  Hour in 24
# print(month)
# month=x.strftime("%I")  # return hr in 12
# print(month)



# # number guessing game python(using random module)

# # user enter num and com generate randomnumber and out put show your guess number is low ,high..


# userNumber=int(input("enter your nameber:"))
# computerNumber=random.randrange(1,101)

# if userNumber>computerNumber :
#     print("computer number:",computerNumber)
#     print("your guess number is too high")
# elif userNumber<computerNumber:
#     print("computer number:",computerNumber)
#     print("your guess number is too low")
# else: 
#     print("computer number:",computerNumber)
#     print("your guessing is correct")







    # project -<  Rock Paper scissor game (using random module)
# rules :
# scissor vs paper ->scissor win
# rock vs scissor ->rock win
# paper vs rock ->paper win

# 5 var loop and count the score who's is win
import random 
l=["rock","paper","scissor"]



while True:
    computer_count=0
    user_count=0
    user_choice=int(input('''
Game Start........
1.Yes
2.No | Exit
'''))

    if user_choice==1:
        for i in range(1,6):
            userInput=int(input('''
choose your move :
1.rock
2.paper
3.scissor
'''))

            if userInput==1:
                us="rock"
            elif userInput==2:
                us="paper"
            elif userInput==3:
                us="scissor"

            computer_choice=random.choice(l)
            
            if us==computer_choice:
                print(f"your choice:{us}")
                print(f"computer choice: {computer_choice}")
                print(" game draw")
                user_count+=1
                computer_count+=1
            elif (us=="rock" and computer_choice=="scissor") or (us=="paper" and computer_choice=="rock") or (us=="scissor" and computer_choice=="paper"):
                print("compuer value:",computer_choice)
                print("user value:",us)
                print("you win")
                user_count+=1
            else:
                print("compuer value:",computer_choice)
                print("user value:",us)
                print("computer  win")
                computer_count+=1   
            
        if user_count==computer_count:
            print("final game draw")    
            print("user score",user_count)
            print("computer count",computer_count)
        elif user_count>computer_count:
            print("You win the game")
            print("user score",user_count)
            print("computer count",computer_count)
        else:
            print("Computer win the game")    
            print("user score",user_count)
            print("computer count",computer_count)
    else:
        break;    






# pickle in python -it is a powerfula algo for serializing and deseriaalizing a python object structure.         serialize means store    and deserialize means read data


# pickle has 2 method main : 1 is dump ->used for sserialize object and 2.is load->de serialize  data stream 

import pickle

l=[10,20,30,40]

# Write the data to a binary file
with open("write_data.txt", "wb") as file:  # Open in write-binary mode
    pickle.dump(l, file)




