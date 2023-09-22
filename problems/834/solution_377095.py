def media_matriz(matriz):
    """Dá a média de todos os números da matriz
    	list -> float
        Parameters:
        matriz: Matriz de inteiros não vazia
        
        Returns:
        Média dos números da matriz (com duas casas decimais)
    """
    
    soma = 0 
    tamanho = 0
    media = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tamanho = tamanho + 1
            soma = soma + matriz[i][j]
            media = soma/tamanho
            
    return round(media,2)