def conta_numero(numero, matriz):
    """Função que recebe um numero inteiro e uma matriz de inteiros de tamanho qualquer,
    retornando quantas vezes aquele numero aparece na matriz
    entrada: int, list(list)
    retorno: int"""
    qtas_vezes= 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            qtas_vezes+= matriz.count(numero)
    return qtas_vezes