def filtra_pares(a, b, c, d):
    w = a % 2
    x = b % 2
    y = c % 2
    z = d % 2
    if  w == 0:
        if x == 0:
            if y == 0:
                if z == 0:
                    return a, b, c, d