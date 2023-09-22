def repetidos(numeros:list)-> int:
    
    numeros_repetidos = int
    i = 0
    ocorrencia = 0
    
    while i < len(numeros):
        
        if (numeros[i] < 0):
            numeros_repetidos = i
            ocorrencia += 1
            
        i = i + 1
        
    return numeros_repetidos