def filtra_pares(A):
    """analisa os 4 números inteiros presentes na tupla de entrada e retorna os valores 
    pares"""
    a, b, c, d = A[1], A[2], A[3], A[4]
    resto1 = a%2
    resto2 = b%2
    resto3 = c%2
    resto4 = d%2
    if resto1 == 0:
        return a