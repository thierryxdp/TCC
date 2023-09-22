def repetidos(lista):
    
    numeros_repetidos = []
    i = 0
    ocorrencia = 0
    
    while i < len(lista):
        
        if (lista[i] == lista [i-1]):
            ocorrencia += 1
            
        i = i + 1
        
    return ocorrencia