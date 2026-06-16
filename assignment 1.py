print("Name: John Doe")
print("College: ABC College")
print("Favorite Programming Language: Python")


name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello", name + ", you are", age, "years old.")



# Creating variables
student_name = "Sham"
roll_number = 101
percentage = 85.5
passed_status = True

# Printing values in a formatted way
print("Student Details")
print("---------------")
print("Name:", student_name)
print("Roll Number:", roll_number)
print("Percentage:", percentage, "%")
print("Passed:", passed_status)


name1 = "Sham"
student_name = "Sham"
class_name = "BCA"
total_marks = 450
user_name = "sham123"


# Variables of different data types
num = 25              # int
price = 99.99         # float
name = "Sham"         # str
is_passed = True      # bool

# Print values and their data types
print(num, type(num))
print(price, type(price))
print(name, type(name))
print(is_passed, type(is_passed))


# Take two numbers as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and display the sum
sum = num1 + num2

print("Sum =", sum)



# Take a decimal number as input
decimal_num = float(input("Enter a decimal number: "))

# Convert to integer and string
integer_num = int(decimal_num)
string_num = str(decimal_num)

# Display converted values
print("Original Decimal Value:", decimal_num)
print("Integer Value:", integer_num)
print("String Value:", string_num)


age = input("Enter your age: ")

print("Value entered:", age)
print("Data type:", type(age))
age = int(input("Enter your age: "))

print("Value entered:", age)
print("Data type:", type(age))


# Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform arithmetic operations
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
print("Modulus =", num1 % num2)


# Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Comparison operations
print("Greater than (num1 > num2):", num1 > num2)
print("Less than (num1 < num2):", num1 < num2)
print("Equal to (num1 == num2):", num1 == num2)
print("Not equal to (num1 != num2):", num1 != num2)



# Login credentials
username = input("Enter username: ")
password = input("Enter password: ")

# Check login using logical operator
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")


    # Take input from user
num = float(input("Enter a number: "))

# Check condition
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


    # Take marks as input
marks = float(input("Enter your marks: "))

# Determine grade
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")


    # Take input from user
num = int(input("Enter a number: "))

# Check even or odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


    # Take age as input
age = int(input("Enter your age: "))

# Determine age group
if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")


    # Simple calculator using if-elif-else

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print("Result =", num1 + num2)

elif choice == "2":
    print("Result =", num1 - num2)

elif choice == "3":
    print("Result =", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid choice")


    # Print numbers from 1 to 20 using for loop

for i in range(1, 21):
    print(i)


    # Print even numbers between 1 and 50

for i in range(1, 51):
    if i % 2 == 0:
        print(i)


        # Multiplication table of a user-input number

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Print numbers from 10 to 1 using while loop

i = 10

while i >= 1:
    print(i)
    i -= 1


# Calculate sum of numbers from 1 to 100

total = 0

for i in range(1, 101):
    total += i

print("Sum of numbers from 1 to 100 is:", total)


# Count number of digits in a number

num = input("Enter a number: ")

# Remove negative sign if present
num = num.lstrip("-")

print("Number of digits:", len(num))


# Print numbers from 1 to 20, stop at 15

for i in range(1, 21):
    if i == 15:
        break
    print(i)



# Print numbers from 1 to 20, skipping multiples of 3

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


# Password checking system using while loop

correct_password = "1234"

password = input("Enter password: ")

while password != correct_password:
    print("Incorrect password. Try again.")
    password = input("Enter password: ")

print("Login successful!")


# Print star pattern

for i in range(1, 6):
    print("*" * i)


# Multiplication table from 1 to 5 using nested loops

for i in range(1, 6):          # outer loop (tables 1 to 5)
    print("Table of", i)
    for j in range(1, 11):     # inner loop (1 to 10)
        print(i, "x", j, "=", i * j)
    print()  # blank line between tables


# Number square pattern

for i in range(1, 5):
    print(str(i) * 4)


# List of 5 student names
students = ["Sham", "Ravi", "Anita", "John", "Meera"]

# Print required details
print("First student:", students[0])
print("Last student:", students[-1])
print("Total number of students:", len(students))


# Take 5 numbers from user and store in a list

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

print("List of numbers:", numbers)


# Create a sample list
numbers = [5, 2, 9, 1, 7]

print("Original list:", numbers)

# append()
numbers.append(10)
print("After append(10):", numbers)

# remove()
numbers.remove(2)
print("After remove(2):", numbers)

# sort()
numbers.sort()
print("After sort():", numbers)

# pop()
removed_item = numbers.pop()
print("After pop():", numbers)
print("Removed item:", removed_item)


# List of elements
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# Print all elements using loop
for fruit in fruits:
    print(fruit)


# List of numbers
numbers = [10, 25, 5, 80, 15]

# Maximum value
print("Maximum value:", max(numbers))

# Minimum value
print("Minimum value:", min(numbers))

# Sum of all elements
print("Sum of all elements:", sum(numbers))



# List of 10 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# First 5 elements
print("First 5 elements:", numbers[:5])

# Last 3 elements
print("Last 3 elements:", numbers[-3:])

# Alternate elements
print("Alternate elements:", numbers[::2])


# Create a tuple
person = ("Sham", 22, "Goa")

# Print values separately
print("Name:", person[0])
print("Age:", person[1])
print("City:", person[2])


# Create a tuple
person = ("Sham", 22, "Goa")

print("Original tuple:", person)

# Try to change a value (this will cause an error)
person[1] = 25

print("Modified tuple:", person)


# Tuple with 5 numbers
numbers = (10, 25, 5, 80, 15)

# Find max, min, and sum
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Total sum:", sum(numbers))


# Tuple packing
student = ("Sham", 22, "Goa", 85.5)

# Tuple unpacking
name, age, city, marks = student

# Display values
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Marks:", marks)


# Mini ATM Menu using loop and conditionals

balance = 1000  # initial balance

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your current balance is:", balance)

    elif choice == "2":
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print("Withdrawal successful!")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == "3":
        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        print("Deposit successful!")
        print("Updated balance:", balance)

    elif choice == "4":
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")


# Student Result Management Program

# Store student marks in a list
marks = []

# Take input for 5 subjects
for i in range(5):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

# Calculate average
total = sum(marks)
average = total / len(marks)

# Find highest marks
highest = max(marks)

# Display grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

# Display results
print("\n----- STUDENT RESULT -----")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest Marks:", highest)
print("Grade:", grade)