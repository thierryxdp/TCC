def fn(num):
    if num % 2 == 0:
        return True
    else:
        return False
def filtra_pares(a,b,c,d):
    tup = [a, b, c, d]
    filtro = filter(fn, tup)
    return tuple(filtro)#Start your python function here