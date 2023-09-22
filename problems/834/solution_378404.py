def media_matriz(matriz):
    '''funcao que retorna a media de 
    uma dada matriz não vazia
    entrada: lista
    saida: float
    '''
    divisor = len(matriz)
    for linha in range(len(matriz)):
        for indice in range(len(matriz[linha])):
            matriz[linha][indice]= matriz[linha][indice]/divisor
            round(matriz[linha][indice],2)
    return matriz