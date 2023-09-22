#função que retorna quantos bolos seram possiveis o João fazer com os materias farinha(A), ovos(B) e leite(C)
#int, int, int -> int
def bolo(A, B, C):
    K = round(A/2, -0.5)
    L = round(B/3, -0.5)
    M = round(c/5, -0.5)
    return (K + L + M)/10