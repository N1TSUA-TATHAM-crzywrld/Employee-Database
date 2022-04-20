name = ["Bob", "sally", "Susan", "gertrude"]
position = ["manager", "intern", "HR", "accounting"]
tenure = ("3 years", "10 years", "11 years", "1 years")

data = list(zip(name, position, tenure))

index_one = (data)[0]
index_two = (data)[1]
index_three = (data)[2]
index_four = (data)[3]

query = input("Please select an index... if your unsure which index you need type ' search ' ")
if (query) == "search":
	lookup = input("Enter a NAME. ")
	x = name.index(lookup)
	print(f"index {x + 1}")
elif (query) == ("index one"):
	print(index_one)
elif (query) == ("index two"):
	print(index_two)
elif (query) == ("index three"):
	print(index_three)
elif (query) == ("index four"):
	print(index_four)
else:
	print("invalid entry")


	