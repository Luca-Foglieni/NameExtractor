from random import randrange

names = open("names.txt", "r")

list = names.readlines()

try:
    print(list)
    print(list[randrange(len(list))])
except ValueError:
    print("The name list is empty. Populate it before running the extraction.")