import random

file = input('Enter path to file to open: ')
output = input("Enter output file (corrupted file): ")

with open(file,"rb") as b:
    stuff = b.read()

newStuff = list(stuff)

index = 0

for char in newStuff:
    if index == 1 or 3 or 6 or 11:
        newStuff[index] = ord(random._urandom(1))
        index += 1
    else:
        index += 1

newNewStuff = bytes(newStuff)

with open(output,"wb") as w:
    w.write(newNewStuff)

