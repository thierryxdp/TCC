def media_matriz(matriz):
    '''Esta função retorna a média de todos o números da
    matriz inserida.
    list -> float'''
    
    termos= 0
    soma=0
    
    for indice in range(len(matriz)):
        for numero in range(len(matriz[indice])):
            soma=soma+matriz[numero]
        termos= termos+1
        media= soma/termos
        
    return media