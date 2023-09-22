def media_matriz(matriz):
    """
    Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz com duas casas decimais de precisao;
    list->float
    """
    lista = []
    soma = 0
    for i in matriz:
        lista += matriz[i]
        for numero in lista:
            soma += numero
    return soma/len(matriz)