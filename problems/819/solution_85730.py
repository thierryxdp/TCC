def filtraMultiplos(l,n):
    i=0
    acumulador=0
    while i < len(l)):
        if (l[i]//n)%2 ==0:
            acumulador+= l[i]
    return acumulador