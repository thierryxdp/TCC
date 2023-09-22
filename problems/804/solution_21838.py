def filtra_pares(a,b,c,d):
    return res(a) + res(b) + res(c) + res(d)
def res(x):
    if x % 2 == 0:
        return x
    else:
        return "none"