def faltante(lista):
    i=0
    a=list(range(len(lista)))[1:]
    falta=0
    
    while i<len(a):
        if a[i]!=lista[i]:
            falta+=a[i]
        else:
            i=i+1
    return falta