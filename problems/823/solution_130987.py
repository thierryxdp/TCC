def faltante(lista):
    lista.sort()
    i, a, b=0, 0, 0
    n=len(lista)-1
    if lista[0]!=1:
        return 1
    while i<n:
        a=lista[i]
        i+=1
        b=lista[i]
        if(b!=a+1):
            return a
    n+=1
    a=lista[n]
    a+=1
    return a