#Ques_1

print('#Ques_1')
#given information
my_string = "Python is a case sensitive language"
#a
print(len(my_string))
#b
print(my_string[::-1])
#c
print(my_string[10:-9])
#d
print(my_string.replace("a case sensitive" , "object oriented"))
#e
print(my_string.index("a"))
#f
print(my_string.replace(" " , ""))





#Ques_2
print('#Ques_2')
#Providing the information
name = 'Garv Bansal'
SID = '21104085'
Department_name = 'EE'
CGPA = "9.9"
#Final answer
print('Hey, {} Here!'.format(name))
print('My SID is {}'.format(SID))
print('I am from {} department and my CGPA is {}'.format(Department_name, CGPA))





#Ques_3
print('#Ques_3')
#Given information
a=56
b=10
#a
print(a&b)
#b
print(a|b)
#c
print(a^b)
#d
print(a<<2)
print(b<<2)
#e
print(a>>2)
print(b>>4)





#Ques_4
print('#Ques_4')
# Take three numbers from user
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
num_3 = float(input("Enter third number: "))

#impliment the if-else statement
if (num_1 > num_2) and (num_1 > num_3):
   largest = num_1
elif (num_2 > num_1) and (num_2 > num_3):
   largest = num_2
else:
   largest = num_3
   
#print the result 
print("The largest number is",largest)






#Ques_5
print('#Ques_5')
#Take the input from the user
user = str(input("enter anything u want: "))
user_one = user.split()

#apply the for condition and print the required answers
for i in user_one:

    if i == 'name':
        print('Yes')
    else:
        print('No')



        


#Ques_6
print('#Ques_6')
#Take the sides of the triangle
a = float(input('Enter the 1st side:  '))
b = float(input('Enter the 2nd side:  '))
c = float(input('Enter the 3rd side:  '))

#Convert them to integers as asked in the question
num1 = int(a)
num2 = int(b)
num3 = int(c)

#apply the else-if statements and print the required answer
if num1 > (num2 + num3):
    print('No')

elif num2 > (num1 + num3):
   print('No')

elif num3 > (num1 + num2):
   print('No')
   
else:   
    print('Yes')     
        
















