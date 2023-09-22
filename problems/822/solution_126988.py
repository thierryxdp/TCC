def repetidos(lista):
    contador=0
    i=1
    while i<len(lista):
        if lista[i]==lista[i-1]:
            contador=contador+1
        i=i+1
    return contador