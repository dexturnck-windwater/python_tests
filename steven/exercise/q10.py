'''
10. Ask the user to enter 10 numbers.
    Store them in a list.
    Then use a loop to print only the numbers greater than 50.
'''

list1=[]

for x in range(1,10,1):
    input1=int(input('please enter 10 numbers: '))
    list1.append(input1)

print('numbers greater than 50: ')

for x in list1:
    if x > 50:
        print(x)
