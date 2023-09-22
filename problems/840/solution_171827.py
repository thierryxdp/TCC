import math
def bolos (a,b,c):
    if a>=2 and b>=3 and c>=5:
        return math.floor((a/2 + b/3 + c/5)/3)
    else:
        return 0