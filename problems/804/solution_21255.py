def filtra_pares(a):
    tup = [a,b,c,d]
    def par(x):
        if x % 2 == 0:
            return True
        else:
            return False
    nova = filter(par, tup)
    return list(nova)