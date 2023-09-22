import math 
def primo(a):
    d = True
    b = int(math.sqrt(a))
    for e in range(b):
        if (a//(e + 2))*(e + 2) == a:
            d = False
    return d