def repetidos(numeros):
    indice = 1
    quant_repetidos = 0
    
    while indice < len(numeros):
        if numeros[indice] == numeros[indice - 1]:
            quant_repetidos += 1
            indice += 1
            
        else:
            indice += 1
            
    return quant_repetidos