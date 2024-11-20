##-------------------------------------------------phone number validation thing
#11-20-24
# while True:
#     phonenumber=input("enter phone number: ")
#     if phonenumber.startswith("9")==True or phonenumber.startswith("8")==True:
#         print("phone number accepted")
#         break
#     else:
#         print("phone number not accepted, try again")

##--------------------------------------------------------email validation thing

# while True:
#     email=input("enter ur email")
#     if email.endswith(".sg"):
#         print("valid email")
#         break
#     else:
#         print("invalid email")
# 
# 

##----------------------------------------------------------------------planet list thing
# planets=['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']
# #extract the value in the list 
# print(planets[6])
# #overwrite the existing item in the list
# planets[2]="whatever"
# print(planets[2])
# #adding a new value to the list at the back
# planets.append("pluto")
# print(planets)
# #adding a new value to the list but in any position
# planets.insert(3,"idk")
# print(planets)
'''
# ##______________________________________________removing an item from the list
# #delete method (if u know exactly what u want to delete but the index)
# del(planets[0])
# print(planets)
# #remove method (if u know exactly what u want to delete but the string name)
# planets.remove("venus")
# #pop method (always removes the last item from the list)
# planets.pop()
# print(planets)
# #len() to check the length of the list(how many items)
# print("there are",len(planets),",in total")
# #for loop in list
# for p in planets:
#     print("someday i will visit",p)
# #assigning a new value for every item
# for i in range(len(planets)):
#     planets[i]="new "+planets[i]

# print(planets)
'''

'''
2020 - Task 2 [10]
The following program checks it the personal identification number (PIN) 
entered for a locker is correct. There are 10 lockers available and the 
correct PIN for each locker is stored in an array.
A PIN cannot start with the digit 0.

The program allows the user to enter the number of the locker they 
want to open, and a PIN. It checks if the PIN is correct for that locker.
'''
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: "))
# pin = float(input("PLease enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")

'''
1.	Edit the program so that it converts the PIN input 
by the user to an integer.
Save your program
[1] 
'''
# Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: "))
# pin = int(input("PLease enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")

'''
2.	Edit the program to only accept a locker number between 1 and 10 
(inclusive) to be input. A suitable error message must be displayed 
if the locker number input is not in this range. The program must 
loop until a valid locker number is input.
Save your program.
[3]
'''
# Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# while True:
#     while True:
#         locker = int(input("Please enter the locker you would like to open: "))
#         if locker >=1 and locker <=10:
#             print("valid locker number")
#             break
#         else:
#             print("invalid locker number, try again")
        
#     while True:
#         pin = int(input("PLease enter the PIN for the locker: "))
#         if pin == arraypins[locker-1]:
#             print("The locker is open.")
#             break
#         else: 
#             print("Incorrect PIN for that locker")
#     break

'''
3.	Edit the program to only accept a PIN of 4 digits to be 
entered by the user. A suitable error message must be displayed 
if an incorrect input is given. The program must loop until the PIN 
input is 4 digits.
Save your program
[3]
'''
# # Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# while True:
#     while True:
#         locker = int(input("Please enter the locker you would like to open: "))
#         if locker >=1 and locker <=10:
#             print("valid locker number")
#             break
#         else:
#             print("invalid locker number, try again")
        
#     while True:
#         pin = int(input("PLease enter the PIN for the locker: "))
#         if len(str(pin))==4:
#             print("valid locker pin length")
#             if pin == arraypins[locker-1]:
#                 print("The locker is open.")
#                 break
#             else: 
#                 print("Incorrect PIN for that locker")
#         else:
#             print("invalid locker pin length")
#     break

'''
4.	Edit the program to loop until the user inputs both a 
correct locker number and the matching PIN for that locker.
Save your program.
[3]
'''
# # Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# #while True:
# while True:
#     locker = int(input("Please enter the locker you would like to open: "))
#     if locker >=1 and locker <=10:
#         print("valid locker number")
#         pin = int(input("PLease enter the PIN for the locker: "))
#         if len(str(pin))==4:
#             print("valid locker pin length")
#             if pin == arraypins[locker-1]:
#                 print("The locker is open.")
#                 break
            
#             else: 
#                 print("Incorrect PIN for that locker")
                
#         else:
#             print("invalid locker pin length")
            
#     else:
#         print("invalid locker number, try again")
    

"""
MOCK Question - Task 3 [10]

The following program manages a list of scores for a competition. 
The scores are stored in a list, 
and the program allows the user to view the scores or add a new score.
"""
# scores = [8, 7, 9, 10, 6]
# choice = int(input("Enter 1 to view scores, or 2 to add a new score: "))
# if choice == 1:
#     print("Scores:", scores)
# elif choice == 2:
#     new_score = int(input("Enter the new score: "))
#     scores.append(new_score)
#     print("Updated scores:", scores)
# else:
#     print("Invalid choice.")

###
"""
1. Modify the program to ensure that only scores between 1 and 10 can be added.
   Display an error message and prompt the user again if the score is invalid.
   Save your program.
   [3]
"""
# Write and test your code here


### end question
"""
2. Edit the program to display the number of scores in the list when 
   the user selects to view the scores.
   Save your program.
   [2]
"""
# Write and test your code here


###
"""
3. Extend the program to allow the user to remove a specific score from the list.
   The user must enter the exact score they wish to remove.
   If the score is not in the list, display an error message.
   Save your program.
   [3]
"""
# Write and test your code here


###
"""
4. Enhance the program to loop until the user chooses to exit.
   Display a menu with options to view scores, add a score, remove a score, or exit.
   Save your program.
   [2]
"""
# Write and test your code here

##----------------------------------------------------dictionary thing  

# shop_price={'hamburger':7.5,'pasta':15,'pizza':25,'food':20}
# #how to retrieve the value of an item
# print(shop_price['hamburger'])
# #how to change the value of an item
# shop_price['hamburger']=10
# print(shop_price)
# #how to add new key value to the dictionary, same as changing value of item but with new name
# shop_price['sdsdsdsdsdsdsds']=120
# print(shop_price)
# #how to delete a key value from the dictionary
# del(shop_price['hamburger'])
# print(shop_price)
# #looping through all keys in a dictionary (item=name of key)
# for item in shop_price:
#     print(item)

# #check if a key value exists in a dictionary
# if "pasta" in shop_price:
#     print("yes it is present")  
# else:
#     print("we dont have it")                              


##question thing
shop_price={'hamburger':7.50,'pasta':15,'pizza':25,'food':20}
wallet=100
bill=0
while True:
    item=input("what do u want to eat, type finish to finish: ")
    if item in shop_price:
        print("we have this food in the menu, added $",shop_price[item],"to bill")
        
        bill=bill+shop_price[item]
        print("total amount payable: $",bill)
    elif item=="finish":
        wallet=wallet-bill
        if wallet<0:
            print("you dont have enough money")
            wallet=wallet+bill
            break
        elif bill==0:
            print("u never ordered anything but ok")
            break
        else:
            print("okay deducted")
            print("amount left in wallet: $",wallet)
            break
    else:
        print("we dont have it in the menu")
    