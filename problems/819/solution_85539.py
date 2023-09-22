def filtraMultiplos(l,n):
    mult=[]
    proximo=0
    while proximo <len(l):
        if l[proximo]%n == 0:
            list.append(mult, l[proximo])
        proximo= proximo + 1
    return mult