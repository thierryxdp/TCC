def filtra_pares(a, b, c, d):
    A = a % 2
    B = b % 2
    C = c % 2
    D = d % 2
    if A == 0 and B != 0 and C != 0 and D != 0:
        return a,