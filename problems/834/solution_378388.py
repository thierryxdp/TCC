def media_matriz(m):
    """função que recebe uma matriz de inteiros não vazia e retorna a média de todos os números da matriz
	list -> float"""
    
    soma = 0
    
    for lin in matriz:
        for num in lin:
            soma = soma + num
        media = soma/(len(m) * len(m[0]))
        
    return round(media, 2)