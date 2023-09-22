def media_matriz(matriz):
    """Retorna a média de todos os números da matriz dada de entrada.
    lista --> float"""
    
    quantidade = []
    linhas = []
    
    
    for i in range(len(matriz)):
        list.append(linhas,i)
        for j in range(len(matriz[i])):
            list.append(quantidade,matriz[i][j])
            
            
    media_denominador = len(matriz)*len(matriz[0])
            
    return round((sum(quantidade)/media_denominador),2)