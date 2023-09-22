def posLetra(texto,letra,n):
    
    if n>texto.count(letra):
        return -1
    i=0
    Oc=[]
    while i<len(texto):
        if texto[i] in letra:
            list.append(Oc,n)
        i = i + 1
    return Oc[n-1]