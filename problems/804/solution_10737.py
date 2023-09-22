def filtra_pares(a, b, c, d):
    if a % 2 == 0:
        if b % 2 == 0:
            if c % 2 == 0:
                if d % 2 == 0:
                    return (a, b, c, d)
    elif a % 2 == 0:
        if b % 2 == 0:
            if c % 2 == 0:
                if d % 2 != 0:
                    return (a, b, c)