def media_matriz(matriz):
    """
    Dada uma matriz de inteiros nao vazia, retorna-se a media dos numeros
    contidos na matriz com 2 casas decimais.
    Entrada: matriz -> list(lists)
    Retorna: float
    """
    soma = 0
    q = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
            q = q + 1
    return round((soma/q),2)