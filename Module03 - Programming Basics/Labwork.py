# Lab 3-4 Script that adds two numbers together, saves to a file, and continues to run till user types in exit

useradd = open("Addition.txt", "a")

userlist = []
numiterator = 0

userlist[numiterator] = input(print("Enter the first number to add (Enter exit to quit): "))

while(True):
    if userlist.lower[numiterator] == 'exit':
        break
    
    else:
        numiterator += 1
        userlist[numiterator] = input(print("Enter the second number to add: "))
        numiterator += 1
        for addition in range(userlist):
            addition += addition
            