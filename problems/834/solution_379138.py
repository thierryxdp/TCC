def media_matriz(matriz):
    """
    	Função que retorna a média de todos os números da 
        matriz dada.
        list(list) -> float
    """
    soma = 0
    for linhas in matriz:
        for numeros in linhas:
            soma += numeros
    divisao = len(matriz)*len(matriz[0])
    return divisao