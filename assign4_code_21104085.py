#q1
print("q1")

def tower_hanoi(n, front , back, a):
    if n == 0:
        return
    
    tower_hanoi(n-1, front , a, back)
    print(f"Move Disk {n} from {front} to {back}")
    tower_hanoi(n-1, a , back, front)

#calling the function
tower_hanoi(3, 'A', 'C', 'B')








#q2
print("\n\nq2.")

#Taking input from the user
no_rows = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursions
print("\nUsing recursions:\n")
#Main code
def pascal_triangle (no_rows , original_no_rows = no_rows):
    if no_rows == 0:
        return
    
    pascal_triangle(no_rows - 1 ,original_no_rows)

    #print the spaces
    print('  '*(original_no_rows - no_rows), end='')

    #starting with always 1
    entry = 1
    for j in range(1, no_rows+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (no_rows - j) // j
    print()
pascal_triangle(no_rows)

#using loops
print("\nUsing loops:\n")
for line in range(1, no_rows+1):

    # same code as recursion
    print('  '*(no_rows - line), end='')

    x = 1
    for j in range(1, line+1):

        print(x, end='   ')

        x = x * (line - j) // j
    print()









    
#q3
print("\n\nq3.")

int_1, int_2 = map(int,input("Enter two numbers: ").split())

quot = int_1 // int_2
remain = int_1 % int_2

#part a
print("a. The quotient and reminder is a callable value.")
print(callable(quot))
print(callable(remain))

#part b
if quot == 0:
    print("b. The quotient is zero")
if remain == 0:
    print("b. The reminder is zero")
if quot != 0 and remain != 0:
    print("b. All the values are non zero")

#part c
list_c = [quot + 4, remain + 4, remain + 5, quot + 5, remain + 5, quot + 6, remain + 6]
res_c = []
for j in range(len(list_c)):
    if list_c[j] > 4:
        res_c.append(list_c[j])
print(f"c. Filtered out numbers: {res_c}")

#part d
set_result = set(res_c)
print("d. Set:",set_result)

#part e
set_frozen = frozenset(set_result)
print("e. Immutable set:",set_frozen)

#part f
print("f. Hash value of the max value from the above set:", hash(max(set_frozen)))








#q4

print("\n\nq4.")
#Main code

class student:
    def __init__(my, student, sid):
        my.name = student
        my.sid = sid
    
    def __del__(my):
        print("Object destructed")

#creating new object
student_1 = student("Garv Bansal", 21104085)
print("Object created")

#print the assigned values
print(f"The name of the student is {student_1.name} and SID is {student_1.sid}.")

#deleting the created object
del student_1










#q5
print("\n\nq5.")

class employees:
    def __init__(my, name, salary):
        my.name = name
        my.salary = salary
    
    def __del__(my):
        print(f"employees {my.name} record deleted")

#creating the records of the employees mentioned in the ques
employee_1 = employees("Mehak", 40000)
employee_2 = employees("Ashok", 50000)
employee_3 = employees("Viren", 60000)

#part_a, updating the salary of mehak
employee_1.salary = 70000
print(f"a. The updated salary of the employee {employee_1.name} is {employee_1.salary}")

#part_b, deleting the record of viren
print("b. ", end='')
del employee_3









#q6
print("\n\nq6.")

#input the word by first friend
word_1 = input("Enter the first word: ")

#input meaningful word with the exact same letters
test_word = input("\nEnter a new meaningful word to test your friendship: ")

#defining dictionary from last assignment
def count_in_dict(word_1):
    count = {}
    list_1 = list(word_1)
    
    n = len(list_1)
    for i in range(n):
        if list_1[i] in count:
            count[list_1[i]] += 1
        else:
            count[list_1[i]] = 1
    return count

#test to verify the letters of the new word
if count_in_dict(word_1) != count_in_dict(test_word):
    print("The friendship is fake!!")

#shopkeeper's input to verify the word's meaning
def userinput():
    answer = input("\nDoes the word makes any sense?(y or n)\n")

    if answer == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif answer == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
