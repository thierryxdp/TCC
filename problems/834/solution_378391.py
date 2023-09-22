def media_matriz(matriz):
    """Recebe uma matriz e retorna a média de todos os seus valores.
    	list -> float"""
    
    soma = 0
    for i in range(0, len(matriz)):
        soma += sum(matriz[i])
            
    return soma/len(matriz[0])