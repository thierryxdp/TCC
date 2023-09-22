def filtra_pares(a,b,c,d):
    """yg"""
    tupla = a,b,c,d
    A = a//2
    B = b//2
    C = c//2
    D = d//2
    filtragem = [A,B,C,D]
    if A == 0 or B ==0 or C ==0 or D ==0:
        return a,b,c,d