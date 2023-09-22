def posLetra(frase,letra,x):
    i=0
    a=list(frase)
    p=0
    while i+1<x:
        list.remove(frase,letra)
        i=i+1
        p=p+1
    if letra in frase:
        return list.index(frase,lista)+p
    else:
        return -1