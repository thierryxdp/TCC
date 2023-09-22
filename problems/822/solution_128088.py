def repetidos(lista):
    i=1
    n=0
    contador=0
    while i<len(lista):
        if lista[i]==lista[n]:
            contador=contador+1
        i=i+1
        n=i-1
    return contador