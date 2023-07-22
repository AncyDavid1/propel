
#1.sort the list in ascending order and print first element
unsorted_list=[34,75,12,45,64,98,76]
sorted_list=unsorted_list.sort()
print(sorted_list[0])


#2.program for table
list_of_numbers=[1,2,3,4,5,6,7,8,9,10]
input=int(input("Enter the number: "))
for number in list_of_numbers:
        print(f"{number}*{input}= ",number*input)


#3.Print the list of numbers which are divisible by 5 and multiple of 8 between 2000 and 2500

list=[]
for i in range(2000,2501):
    if i%5==0 and i%8==0:
        list.append(i)
print(list)


#4.Python program to find second largest number in a list
list1=[1,2,7,5,3,9,6,8]
list1.sort()
print(list1[-2])


#5.Pythonprogram to print odd numbers & even numbers separately
# in al list of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list=[]
even_list=[]
for i in range(1,11):
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(odd_list)
print(even_list)


#6.Program for Reversing a list
list2=[1,2,4,5,7,8]
print("The list is: ",list2)
reverse_list=list2[::-1]
print("The reversed list is: ",reverse_list)


#7.Program to print all odd numbers from 1-50
list3=[]
for i in range(1,51):
    if i%2!=0:
        list3.append(i)
print(list3)


#8.Program to count Even and odd numbers in a list
odd_list=0
even_list=0
for i in range(1,11):
    if i%2==0:
        even_list+=1
    else:
        odd_list+=1
print("The count of odd number:  ",odd_list)
print("The count of even number:  ",even_list)


#9.Write a python program to remove zeros from an IP address("216.08.094.196")

ip_address="216.08.094.196"
ip=ip_address.replace("0","")
print(ip)


#10.Write a Python program that matches a string that has an 'a'
# followed by anything, ending with s

import re
input_string=input("Enter the string")
x=re.match('a+[A-Za-z]+s',input_string)
if x:
    print("The string '{}' matches".format(input_string))
else:
    print("The string doesn't match")


#11.Replace all occurences of 6 with 'six' and
# 10 with 'ten' for the given string 'They ate 6 apples and 10 banana'
string='They ate 6 apples and 10 banana'
new_string=string.replace("6","six")
new_string1=new_string.replace("10","ten")
print(new_string1)



#12.Write a program to check whether a person is eligible for voting or not.
#(accept age from user)
age=int(input("Enter the age"))
if age>18:
    print("You are eligible to vote")
else:
    print("Sorry!!!you are not eligible to vote")


#13.Write a program to calculate the electricity bill (accept number of unit from user) 
#according to the following criteria :
        # Unit                                                     Price
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
user_unit=int(input("Enter the amount: "))
if user_unit<=100:
    print("No Charge")
elif user_unit>100 and user_unit<=200:
    unit_1=user_unit-100
    print("The price is: ",unit_1*5)
elif user_unit>200:
    unit_2=user_unit-200
    unit_3=unit_2*10+100*5
    print("price is",unit_3)

#14.Write a program to accept percentage from the user and
# display the grade according to the following criteria:

        #  Marks                              Grade
	    # > 90                                 A
        # > 80 and <= 90                       B
        #  >= 60 and <= 80                     C
        # below 60
mark=int(input("Enter the mark: "))
if mark>90:
    grade = "GradeA"
elif mark > 80:
    grade = "Grade:B"
elif mark >= 60:
    grade = "Grade:C"
else:
    grade = "Fail"

print(grade)

