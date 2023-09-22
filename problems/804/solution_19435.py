def filtra_pares(a, b, c, d):
    ''
    t=tuple(a,b,c,d)
    return [ n for n in t if n % 2 != 0]