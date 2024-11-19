##----------------------------------password program thing
#assign password variable
# password="idk"
# #ask user to input password
# answer=input("enter the password: ")
# #check 
# if answer==password:
#     print("ur password is correct")
# else:
#     print("womp womp")
    

##-----------------------------------grade calcuator thing
# score=int(input("score: "))
# if score>=100:
#     print("invalid")
# elif score>75:
#     print("A1")
# elif score>=70 and score<=74:
#     print("A2")
# elif score>=65 and score<=69:
#     print("B3")
# elif score>=60 and score<=64:
#     print("B4")
# elif score>=55 and score<=59:
#     print("C5")
# elif score>=50 and score<=54:
#     print("C6")    
# elif score>=45 and score<=49:
#     print("D7")
# elif score>=40 and score<=44:
#     print("E8")
# else:
#     print("F9 retainee sia wah imagine")

##-------------------------------------bulk discount thing
# pennumber=int(input("how many pen u want to buy "))
# cost=pennumber*5
# if pennumber>=100:
#     discount=cost*0.9
#     print("$",discount)
# else: 
#     print("$",cost)
##-------------------------------------guessing game thing
# import random
# randomnum=random.randint(1,100)
# print(randomnum)

# for i in range(7):
#     guess=int(input("guess the number: "))
    
#     if guess == randomnum:
#         print("u got it correct")
#         break
#     elif guess>randomnum:
#         print("too big")
#         if i==5:
#             print("one last chance")
#         elif i==6:
#             print("game over")
#             print("the number was",randomnum)
#             break
#     else:
#         print("too small")
#         if i==5:
#             print("one last chance")
#         elif i==6:
#             print("game over")
#             print("the number was",randomnum)
#             break

##----------------------------------zoo thing
# animal1=input("animal: ")
# animal2=input("animal: ")
# animal3=input("animal: ") 
# if animal1=="monkey" or animal2=="monkey" or animal3=="monkey":
#     print("go bananas")
# else:
#     print("thats a boring zoo")

##------------------------------while loop thing
# count=0
# while count <10:
#     print(count)
#     count=count+1
# ----------------------------------topping thing
# while True:
#     topping=input("what topping do u want ")
    
#     #exit scenario
#     if topping=="exit":
#         print("sending ur order to kitchen")
#         break #break out of the loop
#     else:
#         print ("added",topping,"to")

# havenotanswered1=True
# havenotanswered2=True
# havenotanswered3=True                
        
# while havenotanswered1==True:
#     question1=19
#     answer1=int(input("what is 9+10? "))
#     if answer1==question1:
#         havenotanswered1=False
#         break
#     else:
#         print("wrong answer try again")

# while havenotanswered1==False and havenotanswered2==True:
#     question2=69
#     answer2=int(input("what is 33 x 3? "))
#     if answer2==question2:
#         havenotanswered2=False
#         break
#     else:
#         print("wrong answer try again")

# while havenotanswered2==False and havenotanswered3==True:
#     question3=144
#     answer3=int(input("what is 12 x 12? "))
#     if answer3==question3:
#         havenotanswered3=False
#         print("u answered all riddles correctly")
#         break
#     else:
#         print("wrong answer")

##---------------------------------------------input validation thing
#check that the otp is 4 characters long
# while True:
#     otp=input("enter otp here: ")
    
#     if len(otp)!=4:
#         print("invalid, must be 4 digits. try again")
#     else:
#         print("otp accepted")
#         break



# Question 3 (Range Check):
# Write the input entry and validation code for a program 
# that needs to accept a secondary student's age.

# The age must be between 13 and 16 inclusive.

# If the input is invalid, your code should keep trying 
# by asking for the input to be entered again.

# Sample output:
# Enter age: 12
# Invalid input. Age must be between 13 and 16.
# Enter age: 20
# Invalid input. Age must be between 13 and 16.
# Enter age: 16
# Age accepted.
# ageaccepted=False
# while ageaccepted==False:
#     age=int(input("enter age: "))
#     if age<13:
#         print("Invalid input. Age must be between 13 and 16.")
#     elif age>16:
#         print("Invalid input. Age must be between 13 and 16.")
#     else:
#         print("Age accepted.")
#         ageaccepted=True
        

## -----------------------------------format check thing

# usernameaccepted=False
# while usernameaccepted==False:
#     username=input("enter ur username: ")
#     if username.islower()==False:
#         print("invalid username")
#     else:
#         print("username accepted.")
#         usernameaccepted=True


























































































    
    




    
  
    
     

    

    



    
    




































































































































































































































































































































































































































































