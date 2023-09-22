import math 
def primo(a):
    d = True
    b = int(math.sqrt(a))
    for e in range(b):
        if (a//e)*e == a:
            d = False
    return d