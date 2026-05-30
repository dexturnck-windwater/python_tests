# =========================
# Question 2 — Input, Lists, and Loops
# =========================

"""
Write a program that:

1. Asks the user to input 10 words
2. Stores all the words inside a list
3. Asks the user how many words they want to display
4. Prints the words from the list based on that number

Rules:
- You must use a loop to input the words
- You must use another loop to print the words
- Store the words in a list

Theory Question:
After storing 10 words in a list called words,
can you use:


words[10]

no,because to print the 10th word u use word[9] because it always start form 0
to print the 10th word?

Explain your answer.
"""



word_list=[]
for x in range(1,10,1):
    v1=input("please input a word")
    word_list.append(v1)
v2=int(input("how many wordsto diplay?"))


for x in range(v2):
    print(word_list[x])