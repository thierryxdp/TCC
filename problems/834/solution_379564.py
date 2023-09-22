def media_matriz(matriz):
    """retorna a média de todos os valores da matriz.(list->int)"""
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma=soma + matriz[i][j]
    
    media=soma/(i*j)
   
    return media