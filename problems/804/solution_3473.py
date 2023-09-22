def filtra_pares(a,b,c,d):
    tup = [a, b, c, d]
    def fn(num):
        if num % 2 == 0:
            return True
        else:
            return False
    filtro = filter(fn, tup)
    return tuple(filtro)