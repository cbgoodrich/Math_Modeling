#Charlie Goodrich
#10/02/17
#Repeat_NoRepeat - inputs numberator and denominator, tells you # of repeating numbers

numerator = int(input("Enter a numerator value: "))
denominator = int(input("Enter a denominator value: "))

frac = numerator / denominator

frac1 = str(frac)

print(frac)

if frac1.count("1") > 1:
    a = 1
else:
    a = 0
if frac1.count("2") > 1:
    b = 1
else:
    b = 0
if frac1.count("3") > 1:
    c = 1
else:
    c = 0
if frac1.count("4") > 1:
    d = 1
else:
    d = 0
if frac1.count("5") > 1:
    e = 1
else:
    e = 0
if frac1.count("6") > 1:
    f = 1
else:
    f = 0
if frac1.count("7") > 1:
    g = 1
else:
    g = 0
if frac1.count("8") > 1:
    h = 1
else:
    h = 0
if frac1.count("9") > 1:
    j = 1
else:
    j = 0
if frac1.count("0") > 1:
    i = 1
else:
    i = 0
print("You have",a + b + c + d + e + f + g + h + i, "repeating digits")


