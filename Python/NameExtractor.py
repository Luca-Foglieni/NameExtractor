from random import randrange, sample

names = open("../names.txt", "r")

list = names.readlines()

try:
	extraction = sample(list, len(list))

	print("Press enter to extract itmes one by one.")

	for name in extraction:
		input()
		print(name)

	print("Every item has been extracted.")
except ValueError:
	print("The name list is empty. Populate it before running the extraction.")