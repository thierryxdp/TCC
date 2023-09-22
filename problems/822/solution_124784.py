def repetidos(lista):
    
    contador = 0
    
    for i in lista:
        if lista[i+1] == lista[i]:
            contador = contador + 1
    
    return contador