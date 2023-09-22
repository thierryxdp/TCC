def filtraMultiplos(lista,n):
    d=()
    i=0
    while i<len(lista):
        if lista[i]//n:
            d = d + (lista[i],)
        i=i+1
    return d