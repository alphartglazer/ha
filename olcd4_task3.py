'''
2018 - Task 3 [10]
The following program should identify if a student receives either 
a gold, silver or bronze award for joint achievement in Computing 
and Mathematics. 
Each student has taken a test in Computing and a test in Mathematics. 

The program uses the rules:
- A student receives a gold award for a test score of 
100 or greater in both Computing and Mathematics.

- A student receives a silver award for a test score 
of 100 or greater in Computing or Mathematics. 

They also need a combined Computing and Mathematics
score of 180 or greater.

- A student receives a bronze award for a test score 
of 75 or greater in both Computing and Mathematics.

The test scores are whole numbers only. 
The program finishes when there are no more 
student test scores to be input. 

The award a student receives is output after the 
test scores for that student are input.

There are several syntax and logic errors in the program.

9. Identify and correct the errors in the program so 
that it works according to the rules given. 
Save your program.
[10]

'''
'''
# students = False
# while students == True:
#     comp = input("Enter the Computing test score ")
#     math = int(input("Enter the Mathematics test score ))
#     joint_score = comp + comp
#     if comp > 100 and math > 100:
#         print("Student is awarded a gold award")
#     elif comp >= 100 and math >= 100 or joint_score >= 180:
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if More_scores == 'N':
#         students = True
#     ekse:
#         students = True
'''

# students = True
# while students == True: 
#     comp = int(input("Enter the Computing test score ")) #converted to integer
#     math = int(input("Enter the Mathematics test score"))  #missing "
#     joint_score = comp + math #supposed to be comp+math
#     if comp >= 100 and math >= 100: #fixed more than to more than and equals
#         print("Student is awarded a gold award")
#     elif (comp >= 100 or math >= 100) and joint_score >= 180: #added bracket to comp and math conditions
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if more_scores == "N": #fixed more scores, made 'N' to "N" 
#         students = False
#     else: #fixed ekse to else typo
#         students = True  #flipped true to false

'''
2018 - Task 4 [20]
You have been asked to create a guessing game program.
The program should:
- Allow player 1 to input a whole number between 
1 and 50 inclusive, for player 2 to guess. 

There must be validation present to check that the 
number entered is between 1 and 50 inclusive.

-	Allow player 2 to have 5 guesses to correctly guess 
the number input by player 1. 
You do not need to validate the input for player 2.

-	Output “You guessed the correct number.” 
When player 2 inputs the same number as player 1. 
The game must end if the correct number is guessed.

-	Output “You did not guess the correct number.” 
When player 2 does not input the same number as player 1.

-	Output “Game over!” when player 2 has five incorrect guesses.
'''

'''
10.	Write your program and test that it works.
[10]
'''
# Write and test your code here
# stillhavetries=True
# p1numberisvalid=False
# tries=5
# while p1numberisvalid==False:
#     p1number=int(input("enter a number between 1 and 50: "))
#     if p1number>=1 and p1number <=50:
#         print("valid number entered")
#         p1numberisvalid=True
#     else:
#         print("invalid number entered")
#         p1numberisvalid=False

# while stillhavetries==True:
#     p2guess=int(input("guess the number: "))
#     if p2guess==p1number:
#         print("You guessed the correct number.")
#         break
#     else:
#         print("You did not guess the correct number.")
#         tries=tries-1
#         if tries==0:
#             print("Game over!")
#             break
    
    
##### END QUESTION
'''
11.	When your program is complete, test it for the following:
a.	Test 1 - Player 1 inputs the number 55
b.	Test 2 - Player 1 inputs the number 0
c.	Test 3 - Player 1 inputs the number 10 and player 2 guesses 
    the numbers 15 and 10
d.	Test 4 - Player 1 inputs the number 20 and player 2 guesses 
    the numbers 30, 35, 22, 15, 49
[4]
'''
# Test Your Code ABOVE



##### END QUESTION
'''
12.	
Extend your program to identify if player 2's 
guess is lower or higher than the number input by player 1. 
A suitable message must then be output.

Save your program.
[2]
'''
# Copy your code from above. Write and test your code here
# stillhavetries=True
# p1numberisvalid=False
# tries=5
# while p1numberisvalid==False:
#     p1number=int(input("enter a number between 1 and 50: "))
#     if p1number>=1 and p1number <=50:
#         print("valid number entered")
#         p1numberisvalid=True
#     else:
#         print("invalid number entered")
#         p1numberisvalid=False

# while stillhavetries==True:
#     p2guess=int(input("guess the number: "))
#     if p2guess==p1number:
#         print("You guessed the correct number.")
#         break
#     elif p2guess<p1number:
#         print("your guess is lower than the number.")
#         tries=tries-1
#         if tries==0:
#             print("Game over!")
#             break
#     else:
#         print("your guess is higher than the number.")
#         tries=tries-1
#         if tries==0:
#             print("Game over!")
#             break



##### END QUESTION
'''
13.	

Extend your program to allow player 2 to choose an 
easy, medium or hard game. 

An easy game allows eight guesses, a medium game allows 
six guesses and a hard game allows four guesses.

If player 2 inputs a correct guess, the program must output the 
number of guesses made.

You are not required to validate the input for player 2.

Save your program.
[4]
'''
# Copy your code from above. Write and test your code here
tries=0
difficulty=input("choose the difficulty, easy, medium or hard: ")

if difficulty== "easy":
    tries=8
    print("tries: {}".format(tries))
elif difficulty=="medium":
    tries=6
    print("tries: {}".format(tries))
else:
    tries=4
    print("tries: {}".format(tries))

stillhavetries=True
p1numberisvalid=False
guesses=1
while p1numberisvalid==False:
    p1number=int(input("enter a number between 1 and 50: "))
    if p1number>=1 and p1number <=50:
        print("valid number entered")
        p1numberisvalid=True
    else:
        print("invalid number entered")
        p1numberisvalid=False

while stillhavetries==True:
    p2guess=int(input("guess the number: "))
    if p2guess==p1number:
        print("You guessed the correct number.")
        print("number of guesses: {}".format(guesses))
        break
    elif p2guess<p1number:
        print("your guess is lower than the number.")
        tries=tries-1
        guesses=guesses+1
        if tries==0:
            print("Game over!")
            break
    else:
        print("your guess is higher than the number.")
        tries=tries-1
        guesses=guesses+1
        if tries==0:
            print("Game over!")
            break




##### END QUESTION
