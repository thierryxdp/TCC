def repetidos(lista):
    i = 1
    k = 0
    
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            k += 1
        i += 1
    
    return k