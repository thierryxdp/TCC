def carros(x,y=5):
    import math
    if y == 0:
        y = 5
        z = math.ceil(x/y)
    else:
        z = math.ceil(x/y)
    return z