def posLetra(texto,letra,n):
    i=0
    Oc=[]
    if n>texto.count(letra):
        return -1
    while i<len(texto):
        if texto[i] in letra:
            list.append(Oc,letra)
        i = i + 1
    return Oc[n-1]