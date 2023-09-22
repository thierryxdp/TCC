def media_matriz(matriz):
    '''funcao que retorna a media de 
    uma dada matriz não vazia
    entrada: lista
    saida: float
    '''
    divisor = len(matriz) * len(matriz[0])
    soma = 0
    for linha in range(len(matriz)):
        for indice in range(len(matriz[linha])):
            soma = soma + matriz[linha][indice]
    divisao = soma/divisor
    return round(divisao, 2)