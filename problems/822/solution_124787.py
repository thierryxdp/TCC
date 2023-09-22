def repetidos(lista):
    
    contador = 0
    i = 0
    
    while i < len(lista):
        if lista[i+1] == lista[i-1]:
            contador = contador + 1
        i = i + 1
    
    return contador