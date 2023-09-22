def filtra_pares(a, b=0, c=0, d=0):
    A = (a, b, c, d)
    y = int(A[0]) % 2
    x = A[1] % 2
    z = A[2] % 2
    w = A[3] % 2
    if y == 0:
        return y