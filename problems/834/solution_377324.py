def media_matriz(matriz):
    '''Esta função retorna a média de todos o números da
    matriz inserida.
    list -> float'''
    
    matriz_1=[]
    termos=0
    soma=0
    
    for indice in range(len(matriz)):
        for numero in range(len(matriz[indice])):
            list.append(matriz_1, matriz[numero])
            soma= sum(matriz_1)
        termos= termos+1
        media= soma/termos
        
    return media