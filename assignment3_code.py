#q1
print("#q1")
#taking input from user
text_inp = input('Enter text:')
#Apply the conditions required
if(" "not in text_inp):
    char_count = {}

    for i in text_inp:
        char_count[i] = text_inp.count(i)
#print out the count
    print(char_count)
else:
    print("The input should not start with space")










    
#q2
print("#q2")
#Take input of year from the user
year = int(input("Input a year[1800-2025]: "))
#Apply the constraint using if-else statement
if 1800>=year or year>=2025:
    print("not valid")
else:
    #Checking for leap year
    if (year % 400 == 0):
        
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False
#Take input of month from the user
month = int(input("Input a month [1-12]: "))
#Apply the constraint using if-else statement
if 1>=month  or month >=12:
    print("not valid")
else:
    #  defining the length of months
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30

#Take input of day from the user
day = int(input("Input a day [1-31]: "))
#Apply the constraint using if-else statement
if 1>=day  or day>=31:
    print("not valid")
else:
    #APplying all the needed constraints to get the next date
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))     
    
    
#q3
print("#q3")
# Definig the lists
list_1 = [2,4,8]
list_2 = [num**2 for num in list_1]
#Zipping them together and printing
print(list(zip(list_1,list_2)))



#q4
print("#q4")
#Taking the input for marks
marks = int(input("Marks:\n"))
#Assigning the grades to marks input by user using if-else statement
if(marks>=4 and marks<=10):
    if (marks==4):
        grade_1 = "D"
        grade_2 = "poor"
    elif (marks==5):
        grade_1 = "C"
        grade_2 = "below average"
    elif (marks==6):
        grade_1 = "C+"
        grade_2 = "average" 
    elif (marks==7):
        grade_1 = "B"
        grade_2 = "good" 
    elif (marks==8):
        grade_1 = "B+"
        grade_2 = "very good"
    elif (marks==9):
        grade_1 = "A"
        grade_2 = "excellent"
    elif (marks==10):
        grade_1 = "A+"
        grade_2 = "outstanding"
else:
    print("error")
#Printing the required statement    
print(f"your grade is {grade_1} and your performance is {grade_2}.")   




#q5
print("#q5")
# using n
n = 5
#Applying for loop
for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()



#q6

#q6
print("#q6")
#1sr run
input_YN = "y" 
#Creating dictionaries
dic_1={}
dic_2={}
#Creating list for input values
list_input = ['Y','y','N','n']
#Main code
while input_YN=="Y" or input_YN=="y":
    name = str(input("Enter student name: "))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print ("\nError \nSID can't be negative\n")
    else:
        dic_1.update({sid: name})
        dic_2.update({name : sid})

        input_YN = str(input("Enter Y to continue or N to end:"))
    if input_YN == "N" or input_YN == "n":
        break
    elif (not (input_YN in list_input)):
        print("\nError \nPlease enter valid input['Y' or 'N']")
        input_YN = str(input("\nEnter Y to continue or N to end:"))

                           
                           
#a
#printing the created dictionaries
print("In q6_a")
print("The Dictionary containing ('SID':'Name') is shown below")
print (dic_1)


#b
#printing the  dictionaries sorted by name
print("In q6_b")
list_sorted = sorted(dic_2)
dic_3 = {}
for ele in list_sorted:
     dic_3.update({dic_2.get(ele):ele})
print("The disctionary after sorting according to name:")
print(dic_3)

#c
#printing the  dictionaries sorted by sid
print("in q6_c")
sort_dic_1 = sorted(dic_1)
dic_4 = {}
for te in sort_dic_1:
    dic_4.update({te:dic_1.get(te)})
print("The disctionary after sorting according to the sid:")
print(dic_4)


#d
#code for getting the students name
print("q6_d")
input_sid = int(input("Enter sid to get name of student:"))
output_name = str(dic_1.get(input_sid))
print(f"name of student with sid {input_sid} is {output_name}.")    
    







#q7
print("#q7")
#defining the sequence    
def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-1) + fibo(n-2)
#Taking the input from the user
n = int(input("Enter n\n"))


j = 0
#Required sequence
for i in range(1,n+1):
    print(f"{fibo(i)}",end=",")
    j = j + fibo(i)
    
print(end = "\n")
#Printing the average
print(j/n)





#q8
print("#q8")
#Given values of set
set_1 = {1,2,3,4,5}
set_2 = {2,4,6,8}
set_3 = {1,5,9,13,17}

#applying the conditions for the questions and printing them
set_a = (set_1 | set_2) - (set_1 & set_2)
print("a:", set_a)

set_b = (set_1 | set_2 | set_3) - (set_1 & set_2) - (set_2 & set_3) - (set_1 & set_3)
print("b:",set_b)

set_c = (set_1 & set_2)|(set_2 & set_3)|(set_3 & set_1)
print("c:",set_c )

list_d = []
for i in set_1:
    if i>=1 and i<=10:
        list_d.append(i)
set_d = set(list_d)
print("d:",set_d)


list_e = []
for i in (set_1 | set_2 | set_3):
    if i>=1 and i<=10:
        list_e.append(i)
set_eout = set(list_e)
print("e:",set_eout)
        
    


    
    



        
    














