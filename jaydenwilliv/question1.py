# =========================
# Question 1 — Debugging Data Types
# =========================

"""
A student is making a shopping program for school supplies,
but the code has an error.

Tasks:
1. Find the error
2. Fix the code
3. Explain why the error happens
"""

print("=== Student Shopping Program ===")

student_name = "Luna"
grade = 8

book_price = 15000
pen_price = 5000
notebook_price = 12000

total = 0

print("Calculating total price...")

total = total + book_price
print("Added book")

total = total + pen_price
print("Added pen")

print("Adding notebook...")
total = total + notebook_price

print("Shopping complete")
print("Student:", student_name)
print("Grade:", grade)
print("Total price:", total)

if total > 30000:
    print("You spent a lot!")
else:
    print("Good budgeting!")

#the error is putting double quote on 
'''
error is double wuotr
notebook_price = "12000"
because it is string it usuppose to be interger]
diffrent datatypes
'''