def filtraMultiplos(lista,n):
    i=0
    h=[]
    while i<len(lista):
        if lista[i]%n=0:
            h.append(lista[i])
        i=i+1
    return h