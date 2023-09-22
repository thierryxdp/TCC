def media_matriz(matriz_int):
    """
    Essa função recebe uma matriz de inteiros não vazia e 
    retorna a média de todos os números na matriz_int, com duas 
    casas decimais;
    list -> float
    """
    soma = 0
    for i in matriz_int:
        for j in i:
        	soma += j
    media = soma/len(matriz_int)
    return round(media,2)