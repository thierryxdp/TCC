def media_matriz(A):
    """
    Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz com duas casas decimais de precisao;
    list->float
    """
    nlin = len(A)
    ncol = len(A[0])
    total = nlin*ncol
    soma = []
    for i in range(nlin):
        linha = []
        for j in range(ncol):
             linha.append(A[i][j])
        soma.append(linha)
    return soma/total