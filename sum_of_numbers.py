
# Student Name: Matthew Cires
# Course: CMP 131
# Week: Week 7
# Lab: Lab 01
# Assignment Title: Sum of Numbers
# Date: 10/23/26
print("--- Sum of Numbers ---")
number = int(input("Enter a positive integer: "))
while number <= 0:
    print("Error: Please enter a number greater than 0.")
    number = int(input("Enter a positive integer again: "))
total = 0
for current_number in range(1, number + 1):
    total = total + current_number
print("\n--- Final Result ---")
print(f"Number Enter: {number}")
print(f"The sum of numbers from 1 to {number} is {total}.")
