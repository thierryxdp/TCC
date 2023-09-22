def repetidos(lista):
    i=0
    contador=0
    while i < len(lista):
        if lista[i] in lista[i+1:] :
            contador= contador + list.count(lista,lista[i])
        i=i+1
        
    return contador