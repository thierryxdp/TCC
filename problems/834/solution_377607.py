def media_matriz(matriz):
    """ 
    Função que recebe uma matriz e retorna a média dos números dela.
    list -> float
    
    Parâmetros:
    Entrada: matriz
    Retorna: media da matriz
    """
    soma=0
    
    for i in range(len(matriz)):
        for k in range(len(matriz[0])):
            soma+=matriz[i][k]
        
        tamanho = len(matriz)*len(matriz[0])
        media =soma/tamanho
        
    return round(media,2)