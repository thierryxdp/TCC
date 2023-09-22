import math
def bolos (a,b,c):
    if a>=2 and b>=3 and c>=5 and a<b and a<c:
        return math.floor(a/2)
    else:
        if a>=2 and b>=3 and c>=5 and b<a and b<c:
            return math.floor(b/3)
        else:
            if a>=2 and b>=3 and c>=5 and c<a and c<b:
                return math.floor(c/5)
            else:
                return 0