def media_matriz(matriz):
    """Funcao que recebe uma matriz de inteiros, nao vazia, 
    e retorna a media dde todos os numeros dela.
    list -> float"""
    soma = 0
    total = 0
    for i in matriz:
        for j in i:
            soma += j
        total += len(i)
    return round(soma/total, 2)