#q-1
# Taking two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Calculating the sum
sum = num1 + num2
# Printing the sum
print(f"The sum is: {sum}")

#q-2
# Taking a number as input
number = int(input("Enter a number: "))
# Checking if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

#q-3
# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Taking a number as input
number = int(input("Enter a number: "))
# Calculating the factorial
result = factorial(number)
# Printing the factorial
print(f"The factorial of {number} is {result}.")

#q-4
# Taking the user's name as input
name = input("Enter your name: ")
# Printing the greeting message
print(f"Hello, {name}! Nice to meet you.")

#q-5
# Taking a string as input
user_input = input("Enter a string: ")
# Writing the string to a text file
with open("output.txt", "w") as file:
    file.write(user_input)
print("The string has been written to output.txt.")

#q-6
# Reading the content of a text file and printing it
with open("input.txt", "r") as file:
    content = file.read()
print(content)

#q-7
# Taking a string as input
user_input = input("Enter a string: ")
# Calculating the length of the string
length = len(user_input)
# Printing the length
print(f"The length of the string is: {length}")

#q-8
# Taking two strings as input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
# Concatenating the strings
result = string1 + string2
# Printing the concatenated string
print(f"The concatenated string is: {result}")

#q-9
# Taking the main string and the substring as input
main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
# Checking if the substring is present in the main string
if substring in main_string:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")

#q-10
# Taking a string as input
user_input = input("Enter a string: ")
# Converting the string to uppercase
uppercase_string = user_input.upper()
# Printing the uppercase string
print(f"The uppercase string is: {uppercase_string}")

#q-11
# Function to generate the first n Fibonacci numbers
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence
# Taking the number of terms as input
n = int(input("Enter the number of Fibonacci numbers to generate: "))
# Generating and printing the Fibonacci sequence
fibonacci_numbers = generate_fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")

#q-12
# Function to calculate the sum of the digits of a number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
# Taking a number as input
number = int(input("Enter a number: "))
# Calculating and printing the sum of the digits
digit_sum = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {digit_sum}")

#q-13
from datetime import datetime
# Taking the birth year as input
birth_year = int(input("Enter your birth year: "))
# Calculating the current year
current_year = datetime.now().year
# Calculating and printing the age
age = current_year - birth_year
print(f"Your age is: {age}")

#q-14
# Reading multiple lines of input until an empty line is entered
lines = []
print("Enter lines of text (press Enter to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
# Printing all the lines
print("You entered:")
for line in lines:
    print(line)

#q-15
    import csv
# Function to read and print CSV file data
def read_csv_file(file_path):
    with open("/Users/manavvanshu/file.csv", newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(', '.join(row))
# Taking the CSV file path as input
file_path = input("Enter the path to the CSV file: ")
# Reading and printing the CSV file data
read_csv_file("/Users/manavvanshu/file.csv")

#q-16
# Function to count the frequency of each character in a string
def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
# Taking a string as input
input_string = input("Enter a string: ")
# Counting and printing the frequency of each character
frequency = count_character_frequency(input_string)
print("Character frequency:", frequency)

#q-17
# Function to convert a string to title case
def to_title_case(input_string):
    return input_string.title()
# Taking a string as input
input_string = input("Enter a string: ")
# Converting and printing the string in title case
title_case_string = to_title_case(input_string)
print("Title case:", title_case_string)

#q-18
# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
# Taking two strings as input
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
# Checking and printing if they are anagrams
if are_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")

#q-19
import string
# Function to remove punctuation from a string
def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))
# Taking a string as input
input_string = input("Enter a string: ")
# Removing and printing the string without punctuation
no_punctuation_string = remove_punctuation(input_string)
print("String without punctuation:", no_punctuation_string)

#q-20
# Function to calculate the sum of a list of numbers
def sum_of_numbers(numbers):
    return sum(numbers)
# Taking a list of numbers as input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# Calculating and printing the sum of the numbers
total_sum = sum_of_numbers(numbers)
print("Sum of the numbers:", total_sum)

#q-21
# Function to count occurrences of a specific element in a list
def count_occurrences(lst, element):
    return lst.count(element)
# Taking a list and the element as input
lst = list(map(int, input("Enter the list of numbers separated by space: ").split()))
element = int(input("Enter the element to count: "))
# Counting and printing the occurrences of the element
occurrences = count_occurrences(lst, element)
print(f"The element {element} occurs {occurrences} times in the list.")

#q-22
# Function to find the minimum and maximum values in a list
def find_min_max(lst):
    return min(lst), max(lst)
# Taking a list of numbers as input
lst = list(map(int, input("Enter the list of numbers separated by space: ").split()))
# Finding and printing the minimum and maximum values
min_val, max_val = find_min_max(lst)
print(f"Minimum value: {min_val}, Maximum value: {max_val}")

#q-23
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
# Taking the temperature and conversion choice as input
choice = input("Enter 'C' to convert from Celsius to Fahrenheit, 'F' to convert from Fahrenheit to Celsius: ").upper()
temperature = float(input("Enter the temperature to convert: "))
# Converting and printing the result based on the choice
if choice == 'C':
    print(f"{temperature}°C is equal to {celsius_to_fahrenheit(temperature):.2f}°F")
elif choice == 'F':
    print(f"{temperature}°F is equal to {fahrenheit_to_celsius(temperature):.2f}°C")
else:
    print("Invalid choice!")

#q-24
# Function for simple calculator
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator!"
# Taking two numbers and an operator as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
# Calculating and printing the result
result = calculator(num1, num2, operator)
print(f"The result is: {result}")

#q-25
# Function to copy contents of one file to another
def copy_file(src, dest):
    with open(src, 'r') as src_file:
        content = src_file.read()
    with open(dest, 'w') as dest_file:
        dest_file.write(content)
    print(f"Contents copied from {src} to {dest}")
# Taking source and destination file names as input
src = input("Enter the source file name: ")
dest = input("Enter the destination file name: ")
# Copying the contents
copy_file(src, dest)

#q-26
# Function to check if string starts with a prefix or ends with a suffix
def check_prefix_suffix(string, prefix, suffix):
    return string.startswith(prefix), string.endswith(suffix)
# Taking string, prefix, and suffix as input
string = input("Enter the string: ")
prefix = input("Enter the prefix: ")
suffix = input("Enter the suffix: ")
# Checking and printing the results
starts_with_prefix, ends_with_suffix = check_prefix_suffix(string, prefix, suffix)
print(f"String starts with '{prefix}': {starts_with_prefix}")
print(f"String ends with '{suffix}': {ends_with_suffix}")

#q-27
# Function to convert string into a list of characters
def string_to_char_list(string):
    return list(string)
# Taking a string as input
string = input("Enter the string: ")
# Converting and printing the list of characters
char_list = string_to_char_list(string)
print("List of characters:", char_list)














