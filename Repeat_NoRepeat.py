#Charlie Goodrich
#10/02/17
#Repeat_NoRepeat - inputs numberator and denominator, tells you # of repeating numbers

numerator = int(input("Enter a numerator value: "))
denominator = int(input("Enter a denominator value: "))

frac = numerator / denominator

frac1 = str(frac)

print(frac)

count = frac1.count("3")
print(count)

