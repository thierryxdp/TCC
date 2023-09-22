def media_matriz(matriz_inteiros):
    
    ''' Função que retorna a media de todos
        os números de uma matriz de inteiros,
        com duas casa decimais de precisão.
        list -> float '''
    
    soma = 0
    divisor = 0
    
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            soma += matriz[l][c]
            divisor += 1
    
    media = soma/divisor
    
    return media