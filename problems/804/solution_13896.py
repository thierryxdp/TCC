def filtra_pares(a, b):
    if a%2 == 0 and b%2 == 0:
        return a, b
    if a%2 == 0 and b != 0:
        return a
    if a%2 != 0 and b%2 == 0:
        return b