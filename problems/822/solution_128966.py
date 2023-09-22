def repetidos(lista):
    i=0
    ocorrencias=0
        
    while i<len(lista):
        
        if lista[i-1]==lista[i]:
            ocorrencias=ocorrencias+1
        i=i+1
    return ocorrencias