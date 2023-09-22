def media_matriz(matriz):
    """
    Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz com duas casas decimais de precisao;
    list->float
    """
    tamanho = len(matriz)
    lista = []
    for i in matriz:
        linha = []
        for j in matriz:
            linha.append(A[i] + A[j])
        lista.append(linha)
        soma = 0
        for numero in lista:
            soma += numero
    return soma