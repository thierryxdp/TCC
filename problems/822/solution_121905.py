def repetidos(lista):
    i=0
    contador=0
    while i < len(lista):
        if lista[i] in lista[i:] :
            contador= contador + 1
        i=i+1
        
    return contador