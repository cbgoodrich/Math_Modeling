#Charlie Goodrich
#10/02/17
#Repeat_NoRepeat - inputs numberator and denominator, tells you # of repeating numbers

numerator = int(input("Enter a numerator value: "))
denominator = int(input("Enter a denominator value: "))

frac = numerator / denominator

frac1 = str(frac)

print(frac)

i = 0
while i <= 9:
    if i in frac1:
        print(i)
    i += 1