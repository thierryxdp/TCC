def repetidos(numeros):
    posicao = 0
    vezesRepetidas = 0
    
    while posicao < len(numeros):
        if numeros[posicao] == numeros[posicao - 1]:
            vezesRepetidas += 1
            posicao += 1
            
        else:
            posicao += 1
            
    return vezesRepetidas