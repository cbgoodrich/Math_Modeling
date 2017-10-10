#Charlie Goodrich
#10/02/17
#Repeat_NoRepeat - inputs numberator and denominator, tells you # of repeating numbers

numerator = int(input("Enter a numerator value equal to 1: "))
denominator = int(input("Enter a denominator value between 1 and 100: "))

frac = numerator / denominator

print(frac)

i = 1
counterOf2 = 0 #the counter of factors of two in the denominator
counterOf5 = 0 #the counter of factors of five in the denominator
counterOf3 = 0
""" since the denominator is limited to 100, dividing through
by all the powers of 2 less than 100"""
while i <= 6: 
    if denominator % (2 ** i) == 0:
        counterOf2 += 1
    i += 1
i = 1 

while i <= 2: #same thing with the powers of two above, doing the same with 5
    if denominator % (5 ** i) == 0:
        counterOf5 += 1
    i += 1
i = 1

denominator_2 = denominator / (2 ** counterOf2)
denominator_prime = denominator_2 / (5 ** counterOf5)

print(denominator_prime)







if counterOf2 >= counterOf5:
    print("You have", counterOf2, "non repeating digits")
else:
    print("You have", counterOf5, "non repeating digits")
print(counterOf3)