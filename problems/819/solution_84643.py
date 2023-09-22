def filtraMultiplos(lista,n):
    divisiveis=[]
    i=0
    while i<len(lista):
        if lista[i]/n:
            divisiveis= divisiveis + (lista[i],)
        i=i+1
    return divisiveis