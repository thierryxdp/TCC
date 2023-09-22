def filtra_pares(a,b,c,d):
    tup = [a,b,c,d]
    def par(x):
        if x % 2 == 0:
            return True
        else:
            return False

    nova = filter(par, tup)
    print (list(nova))