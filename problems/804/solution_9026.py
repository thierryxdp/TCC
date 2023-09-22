def filtra_pares(a, b, c, d):
    A = (a, b, c, d)
    y = A[0] % 2
    x = A[1] % 2
    z = A[2] % 2
    w = A[3] % 2
    if y == 0:
        return y