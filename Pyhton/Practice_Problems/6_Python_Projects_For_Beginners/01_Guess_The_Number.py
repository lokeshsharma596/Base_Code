import random
n = random.randrange(1, 21, 1)
g = 0


def Check(g, n):
    return "Guess Higher" if g < n else "Guess Lower" if g > n else "You Won"


while(n != g):
    g = int(input("Enter Number Bw 1-20:"))
    if g in range(1,21):
        print(Check(g, n))
    else:
        print("Alert:Enter Correct")
