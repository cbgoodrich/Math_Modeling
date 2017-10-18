#Charlie Goodrich
#10/18/17
#repeatNoRepeat2.py - tells you the fraction

repeat = int(input("Enter the number of repeating digits: "))

frac = 1/3

num1 = frac * 10**repeat
num2 = num1//1
num3 = 10**repeat - 1

print(num2/num3)