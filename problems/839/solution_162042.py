import math
def carros(p,a=5):
    if a==5:
        c=p/5
        return math.ceil(c)
    else:
        c=p/a
        return math.ceil(c)