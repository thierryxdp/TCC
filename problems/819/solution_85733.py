def filtraMultiplos(l,n):
    i=0
    acumulador=0
    while acumulador < len(l):
        if (l[i]//n):
            acumulador+= l[i]
    return acumulador