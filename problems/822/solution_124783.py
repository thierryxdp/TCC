def repetidos(lista):
    
    contador = 0
    
    for i in lista:
        if i+1 == i:
            contador = contador + 1
    
    return contador