import math
def bolos(A,B,C):
    if (A%2 == 0) and (B%3 == 0) and (C%5 == 0):
        if min(A,B,C)%2 == 0:
            qtd_bolos = A/2
            return A/2
        elif min(A,B,C)%3 == 0:
            qtd_bolos = B/3
            return B/3
        elif:
            qtd_bolos = C/5
            return qtd_bolos
        else:
            return 0