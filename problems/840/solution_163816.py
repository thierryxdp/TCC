#função que retorna quantos bolos seram possiveis o João fazer com os materias farinha(A), ovos(B) e leite(C)
#int, int, int -> int
def bolos(A, B, C):
    K = round(A/2 -0.5)
    L = round(B/3, -0.5)
    M = round(c/5, -0.5)
    if K and L and M >= 1:
        return (K + L + M)/10
    else:
        return