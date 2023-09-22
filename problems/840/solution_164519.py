from math import floor
def bolos(xic_farinha,n_ovos,col_leite):
    a = xic_farinha/2
    b = n_ovos/3
    c = col_leite/5
    return floor(min(a,b,c))