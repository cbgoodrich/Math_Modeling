#Charlie Goodrich
#10/02/17
#Repeat_NoRepeat - inputs denominator, tells you # of repeating numbers

numerator = int(input("Enter a numerator value equal to 1: "))
denominator = int(input("Enter a denominator value between 1 and 50: "))

frac = numerator / denominator

print(frac)

i = 1
counterOf2 = 0 #the counter of factors of two in the denominator
counterOf5 = 0 #the counter of factors of five in the denominator
counterOf3 = 0
counterOf7 = 0
counterOf11 = 0
counterOf13 = 0
counterOf17 = 0
counterOf19 = 0
counterOf23 = 0
counterOf29 = 0
counterOf31 = 0
counterOf37 = 0
counterOf41 = 0
counterOf43 = 0
counterOf47 = 0
""" since the denominator is limited to 50, dividing through
by all the powers of 2 less than 50"""
while i <= 5: 
    if denominator % (2 ** i) == 0:
        counterOf2 += 1
    i += 1
i = 1 

while i <= 2: #same thing with the powers of 2 above, doing the same with 5
    if denominator % (5 ** i) == 0:
        counterOf5 += 1
    i += 1
i = 1

denominator_2 = denominator / (2 ** counterOf2) 
"""finding what's left of the denominator after diving through 
by the powers of 2 that go into it"""

denominator_prime = denominator_2 / (5 ** counterOf5) 
#finding the final denominator after dividing through by the powers of 2 and 5

while i <= 3: #doing the powers thing with 3
    if denominator_prime % (3 ** i) == 0:
        counterOf3 += 1
    i += 1
i = 1

while i <= 2: #doing the powers thing with 7
    if denominator_prime % (7 ** i) == 0:
        counterOf7 += 1
    i += 1
i = 1

while i < 2: #now doing with 11
    if denominator_prime % (11 ** i) == 0:
        counterOf11 += 1
    i += 1
i = 1

while i < 2: #now doing with 13
    if denominator_prime % (13 ** i) == 0:
        counterOf13 += 1
    i += 1
i = 1

while i < 2: #now doing with 17
    if denominator_prime % (17 ** i) == 0:
        counterOf17 += 1
    i += 1
i = 1

while i < 2: #now doing with 19
    if denominator_prime % (19 ** i) == 0:
        counterOf19 += 1
    i += 1
i = 1

while i < 2: #now doing with 23
    if denominator_prime % (23 ** i) == 0:
        counterOf23 += 1
    i += 1
i = 1

while i < 2: #now doing with 29
    if denominator_prime % (29 ** i) == 0:
        counterOf29 += 1
    i += 1
i = 1

while i < 2: #now doing with 31
    if denominator_prime % (31 ** i) == 0:
        counterOf31 += 1
    i += 1
i = 1

while i < 2: #now doing with 37
    if denominator_prime % (37 ** i) == 0:
        counterOf37 += 1
    i += 1
i = 1

while i < 2: #now doing with 41
    if denominator_prime % (41 ** i) == 0:
        counterOf41 += 1
    i += 1
i = 1

while i < 2: #now doing with 43
    if denominator_prime % (43 ** i) == 0:
        counterOf43 += 1
    i += 1
i = 1

while i < 2: #now doing with 47
    if denominator_prime % (47 ** i) == 0:
        counterOf47 += 1
    i += 1
i = 1


if counterOf2 >= counterOf5: #telling to print the highest number of non repeat
    print("You have", counterOf2, "non repeating digits")
else:
    print("You have", counterOf5, "non repeating digits")
"""checks the prime factorization of the denominator, gives you the repeating 
based on the number of each prime factor"""
if counterOf47 >= 1:
    print("You have at most 46 repeating digits")
elif counterOf43 >= 1:
    print("You have at most 42 repeating digits")
elif counterOf41 >= 1:
    print("You have at most 40 repeating digits")
elif counterOf37 >= 1:
    print("You have at most 36 repeating digits")
elif counterOf31 >= 1:
    print("You have at most 30 repeating digits")
elif counterOf29 >= 1:
    print("You have at most 28 repeating digits")
elif counterOf23 >= 1:
    print("You have at most 22 repeating digits")
elif counterOf19 >= 1:
    print("You have at most 18 repeating digits")
elif counterOf17 >= 1:
    print("You have at most 16 repeating digits")
elif counterOf13 >= 1:
    print("You have at most 12 repeating digits, but it's most likely 6")
elif counterOf11 >= 1:
    print("You have at most 10 repeating digits, but it's most likely 2")
elif counterOf7 >= 1:
    print("You have 6 repeating digits")
elif counterOf3 >=1:
    print("You have 1 repeating digit")
else:
    print("You have 0 repeating digits")
