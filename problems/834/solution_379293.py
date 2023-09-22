def media_matriz(A):
    """
    Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz com duas casas decimais de precisao;
    list->float
    """
    nlin = len(A)
    ncol = len(A[0])
    soma = 0
    for i in range(nlin):
        for numero in A:
            soma+=numero
    return (soma/(nlin*ncol))