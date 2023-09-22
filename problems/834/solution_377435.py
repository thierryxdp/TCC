def media_matriz(matriz):
    '''retorna a media de todos os
    numeros inseridos na matriz com 2 casas de precisao
    list(list) -> float'''
    
    soma = 0
    n_elementos= len(matriz)*len(matriz[0])
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            
    return round(soma/n_elementos,2)