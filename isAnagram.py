#input
s1, s2 = input().split()

# One-liner
isAnagram = True if sorted(s1) == sorted(s2) else False

#result
print(isAnagram)
