def repetidos(lista):
    p=1
    i=0
    contador=0
    while i < len(lista):
        if lista[i] in lista[p] :
            contador= contador + 1
        i=i+1
        p=p+1
    return contador