def filtra_pares(a, b, c, d):
    
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        return tuple(a, b, c , d)

    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2>0:
        return tuple(a, b, c)

    if a%2 == 0 and b%2 == 0 and c%2>0 and d%2>0:
        return tuple(a, b)

    if a%2 == 0 and b%2>0 and c%2>0 and d%2>0:
        return tuple(a)

    if a%2 == 0 and b%2>0 and c%2 == 0 and d%2 == 0:
        return tuple(a,c,d)

    if a%2 == 0 and b%2>0 and c%2 == 0 and d%2>0:
        return tuple(a, c)

    if a%2 == 0 and b%2 == 0 and c%2>0 and d%2 == 0:
        return tuple(a, b, d)
   
    if a%2 == 0 and b%2>0 and c%2>0 and d%2 == 0:
        return tuple(a, d)