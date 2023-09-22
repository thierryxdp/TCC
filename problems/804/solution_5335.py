def filtra_pares(x):
	a, b, c, d = x
    if a%2 == 0:
        return x
    else:
        return x-a
    if b%2 == 0:
        return x
    else:
        return x-b
    if c%2 == 0:
        return x
    else:
        return x-c
    if d%2 == 0:
        return x
    else:
        return x-d
    return x