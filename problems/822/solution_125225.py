def repetidos(lista):
    tamanho = len(lista)
    i = 0
    acumulador = 0
    
    while i < tamanho:
        if (lista[i] == lista[i-1]):
            acumulador = acumulador + 1
        else:
            acumulador = acumulador
        
        i = i + 1
        
    return acumulador