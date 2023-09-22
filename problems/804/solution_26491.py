def filtra_pares(ls):
    ln = []
    x = 0
    while x < len(ls):
        if ls[x] % 2 == 0:
        	ls.extend(ls[x])
        x = x + 1
    return ln