#função que retorna quantos bolos seram possiveis o João fazer com os materias farinha(A), ovos(B) e leite(C)
#int, int, int -> int
def bolos(A, B, C):
    import math
    K = round(A/2 -0.5)
    L = round(B/3 -0.5)
    M = round(C/5 -0.5)
    if K and L and M = 1:
        return math.ceil((K + L + M)/10)
    if K and L and M > 1:
        return (A +B+C)/10
    else:
        return 0