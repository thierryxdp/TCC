def filtra_pares(a):
    if a[0] % 2 == 0 and a[1] % 2 == 0 and a[2] % 2 == 0 and a[3] % 2 == 0:
        return a, b, c, d
    elif a[0] % 2 == 0 and a[1] % 2 == 0 and a[2] % 2 == 0:
        return a, b, c
    elif a[0] % 2 == 0 and a[1] % 2 == 0 and a[3] % 2 == 0:
        return a, b, d
    elif a[0] % 2 == 0 and a[2] % 2 == 0 and a[3] % 2 == 0:
        return a, c, d
    elif a[1] % 2 == 0  and a[2] % 2 == 0 and a[3] % 2 == 0:
        return b, c, d
    elif a[0] % 2 == 0 and a[1] % 2 == 0:
        return a, b
    elif a[0] % 2 == 0 and a[2] % 2 == 0:
        return a, c
    elif a[0] % 2 == 0 and a[3] % 2 == 0:
        return a, d
    elif a[1] % 2 == 0 and a[2] % 2 == 0:
        return b, c
    elif a[1] % 2 == 0 and a[3] % 2 == 0:
        return b, d
    elif a[2] % 2 == 0 and a[3] % 2 == 0:
        return c, d
    elif a[0] % 2 == 0:
        return a
    elif a[1] % 2 == 0:
        return b
    elif a[2] % 2 == 0:
        return c
    elif a[3] % 2 == 0:
        return d
    else:
        return 'não tem número par'