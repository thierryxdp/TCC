def repetidos(lista):
    i = 0
    k = 0
    
    while i < len(lista):
        if i != 0:
            if lista[i] == lista[i - 1]:
                k += 1
        i += 1
    
    return k