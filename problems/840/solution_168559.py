from math import*
def bolos(a,b,c):
    if a>=2 and b>=3 and c>=5:
        return floor(((a/2)*0.2)+((b/3)*0.3)+((c/5)*0.5))
    elif a<2 or b<3 or c<5:
        return 0