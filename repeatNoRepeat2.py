#Charlie Goodrich
#10/18/17
#repeatNoRepeat2.py - tells you the fraction

def fn(repeat, norepeat):
    if repeat == 1:
        frac = 1/3
        num1 = frac * 10**repeat
        num2 = num1//1
        num3 = 10**repeat - 1
        print(num2/num3)

fn(1,0)