def media_matriz(matriz):
    """Retorna a média de todos os números da matriz dada de entrada.
    lista --> float"""
    
    quantidade = []
    linhas = []
    colunas = []
    
    for i in range(len(matriz)):
        list.append(linhas,i)
        for j in range(len(matriz[i])):
            list.append(quantidade,matriz[i][j])
            list.append(colunas,j)
            
    media_denominador = max(linhas)*max(colunas)
            
    return (sum(quantidade)/media_denominador)