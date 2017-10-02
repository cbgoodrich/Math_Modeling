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
elif frac1.count("1") == 1:
    A = .5
else:
    a = 0
if frac1.count("2") > 1:
    b = 1
elif frac1.count("2") == 1:
    B = .5
else:
    b = 0
if frac1.count("3") > 1:
    c = 1
elif frac1.count("3") == 1:
    C = .5
else:
    c = 0
if frac1.count("4") > 1:
    d = 1
elif frac1.count("4") == 1:
    D = .5
else:
    d = 0
if frac1.count("5") > 1:
    e = 1
elif frac1.count("6") == 1:
    E = .5
else:
    e = 0
if frac1.count("6") > 1:
    f = 1
elif frac1.count("7") == 1:
    F = .5
else:
    f = 0
if frac1.count("7") > 1:
    g = 1
elif frac1.count("7") == 1:
    G = .5
else:
    g = 0
if frac1.count("8") > 1:
    h = 1
elif frac1.count("9") == 1:
    H = .5
else:
    h = 0
if frac1.count("9") > 1:
    j = 1
elif frac1.count("9") == 1:
    J = .5
else:
    j = 0
if frac1.count("0") > 1:
    i = 1
elif frac1.count("0") == 1:
    I = .5
else:
    i = 0
print("You have", a + b + c + d + e + f + g + h + i, "repeating digits")
print("You have", A + B + C + D + E + F + G + H + I, "non-repeating digits")


