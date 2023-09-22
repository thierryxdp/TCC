def filtra_pares(a, b=0, c=0, d=0):
    A = (a, b, c, d,)
    AA = int(A[0]) % 2
    BB = A[1] % 2
    CC = A[2] % 2
    DD = A[3] % 2
    return A[0],