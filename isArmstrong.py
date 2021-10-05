#input
k = int(input("Enter number"))

#One-liner
isArmstrong = True if k == sum([int(i) ** len(str(k)) for i in str(k)]) else False

#result
print(isArmstrong)
