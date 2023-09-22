def total(ls, d):
    numero = 0
    for r in ls:
        numero += d[r]
    return round(numero, 2)