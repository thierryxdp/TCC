def filtra_pares(elementos):
    a,b,c,d = elementos
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        return (a,b,c,d)
    elif a%2 == 0 and b%2 == 0 and c%2 == 0 and (d%2 > 0 or d%2 < 0):
        return (a,b,c)
    elif a%2 == 0 and b%2 == 0 and (c%2 > 0 or c%2 < 0) and (d%2 > 0 or d%2 < 0):