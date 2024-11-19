'''
The following program allows the weights of 15 bags of rice to be input. 
The correct weight for each bag of rice must be 
between 4.9 kg and 5.1 kg inclusive.
'''
# bags_rice = 15
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")
'''
Open the file RICEBAGS.py
Save the file as MYBAGS_<your name>_<center number>_<index number>.py

1.	Edit the program so that it:
a.	Accepts the weights for only 10 bags of rice.
[1]
'''
# bags_rice = 10
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")
'''
b.	Prints out the message “The bag of rice is the correct weight” 
when a weight entered is between 4.9kg and 5.1 kg inclusive.
[2]
'''
# bags_rice = 10
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     elif bag_weight < lower_bound:
#         print("The bag of rice is underweight")
#     else:
#         print("The bag of rice is the correct weight")
'''
c.	Prints out the number of bags of rice that were underweight, 
as well as the number that were overweight, after the weights of 
all the bags have been entered.
[5]
'''
# bags_rice = 10
# upper_bound = 5.1
# lower_bound = 4.9
# noofoverweight=0
# noofunderweight=0
# correctweight=0
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#         noofoverweight=noofoverweight+1
#     elif bag_weight < lower_bound:
#         print("The bag of rice is underweight")
#         noofunderweight=noofunderweight+1
#     else:
#         print("The bag of rice is the correct weight")
#         correctweight=correctweight+1
# print("no. of overweight: ",noofoverweight,", no. of underweight: ",noofunderweight,", no. of correct weight: ",correctweight)
'''
Save your program.
2.	Save your program as VARBAGS_<your name>_<center number>_<index number>.py
Edit your program so that it works for any number of bags of rice.
Save your program.
[2]
'''
bags_rice = int(input("how many bags of rice are you weighing? "))
upper_bound = 5.1
lower_bound = 4.9
noofoverweight=0
noofunderweight=0
correctweight=0
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice: "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
        noofoverweight=noofoverweight+1
    elif bag_weight < lower_bound:
        print("The bag of rice is underweight")
        noofunderweight=noofunderweight+1
    else:
        print("The bag of rice is the correct weight")
        correctweight=correctweight+1
print("no. of overweight: ",noofoverweight,", no. of underweight: ",noofunderweight,", no. of correct weight: ",correctweight)