def filtra_pares(a, b, c, d):
    w = a/2
    x = b/2
    y = c/2
    z = d/2
    if  w % 2 == 0:
        if b % 2 == 0:
            if c % 2 == 0:
                if d % 2 == 0:
                    return a, b, c, d