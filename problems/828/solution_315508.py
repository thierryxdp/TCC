import math 
def primo(a):
    d = True
    b = int(math.sqrt(a))
    for e in range(b):
        if (a//e + 1)*(e + 1) == a:
            d = False
    return d