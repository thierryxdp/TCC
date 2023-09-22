def repetidos(listaNumeros):
    i = 1
    occRep = 0
    nAnterior = listaNumeros[0]
    
    while i < len(listaNumeros):
        if listaNumeros[i] == nAnterior:
           	occRep += 1
        nAnterior = listaNumeros[i]
        i += 1
        
    return occRep