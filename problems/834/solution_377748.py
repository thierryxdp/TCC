def media_matriz(matriz):
    """Retorna a média de todos os números da matriz dada de entrada.
    lista --> float"""
    
    quantidade = []
    
    
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(quantidade,matriz[i][j])
            
            
    media_denominador = len(matriz)*len(matriz[0])
            
    return round((sum(quantidade)/media_denominador),2)