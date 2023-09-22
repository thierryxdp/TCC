def(A,B,C):
    "função que retorna a quantidade máxima de bolos que João pode fazer "
    import math
    if min(A,B,C)=A:
        return math.floor(A/2)
    if min(A,B,C)=B:
        return math.floor(B/3)
    if min(A,B,C)=C:
        return math.floor(C/5)