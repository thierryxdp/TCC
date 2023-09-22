import math
def bolos(xíc_farinha,n_ovos,col_leite):
    a = xíc_farinha/2
    b = n_ovos/3
    c = col_leite/5
    if a<=b and a<=c:
        return floor(a)
    elif b<=a and b<=c:
        return floor(b)
    else:
        return floor(c)