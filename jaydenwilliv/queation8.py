#=========================
# Question 8 — File Reading and Writing Debugging
# =========================

"""
A student is making a program to save and read
a shopping list from a text file.

The code has mistakes related to lists and file reading.

Tasks:
1. Find the mistakes
2. Fix the code
3. Explain why the mistakes happen
"""

shopping_list = ["apple", "banana", "milk"]

file = open("shopping.txt", "w")

for item in shopping_list:
    file.write(item + "\n")

file.close()

file = open("shopping.txt", "r")

data = file.read()

file.close()

for item in shopping_list:
    print(item.upper())


"""
Theory Questions

1. What does file.read() return?
     reading the file

2. Why does the loop not print:
   APPLE
   BANANA
   MILK

   because item[0] makes it print one by one

3. What happens if this code is used?

 
print(data[0])
it will only print A A A because it onlt prints the first words
Explain your answer.
"""