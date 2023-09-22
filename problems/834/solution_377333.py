def media_matriz(matriz):
    '''Esta função retorna a média de todos o números da
    matriz inserida.
    list -> float'''
    
    soma=0
    termos=0
    linhas=len(matriz)
        
    for indice in range(linhas):
        soma=soma + sum(matriz[indice])
        for j in range(len(matriz[indice])):
            termos=termos+1   
        
    media= soma/termos
            
    return round(media,2)