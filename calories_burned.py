
# Student Name: Matthew Cires
# Course: CMP 131
# Week: Week 7
# Lab: Lab 01
# Assignment Title: Calories Burned
# Date: 10/23/26

print("--- Calories Burned on a Treadmill ---")
calories_per_minute = 3.6
print("Minutes\tCalories Burned")
print("----------------------------")
for minutes in range(5, 31, 5):
    calories_burned = minutes * calories_per_minute
    print(f"{minutes}\t{calories_burned:.1f}")
