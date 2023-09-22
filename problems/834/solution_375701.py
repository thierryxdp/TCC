def media_matriz(matriz):
    '''media_matriz recebe uma matriz e devolve a media de todos os numeros da matriz(com exatamente duas casas decimais de precisão).
    Assume uma matriz de inteiros não vazia.
    list-->float.'''
    soma=0
    quantidade=0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            soma= soma+matriz[linha][coluna]
            quantidade=quantidade+1
    media=soma/quantidade
    return round(media,2)