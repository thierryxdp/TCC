from math import floor
def bolos(a,b,c):
    ''''''
    if a<0 or b<0 or c<0:
        return 0
    else:
        return floor(min(a,b,c))