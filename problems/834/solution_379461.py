def media_matriz(matriz):
    """
    Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz com duas casas decimais de precisao;
    list->float
    """
    soma = 0
    for i in range(len(matriz)):
        for numero in range(len(matriz[0])):
            soma += numero
    return round((soma/len(matriz),2)