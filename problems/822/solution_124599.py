def repetidos(lista):
    
    numeros_repetidos = []
    i = 0
    ocorrencia = 0
    
    while i < len(lista):
        
        if (lista[i] < 0):
            numeros_repetidos = i
            ocorrencia += 1
            
        i = i + 1
        
    return numeros_repetidos