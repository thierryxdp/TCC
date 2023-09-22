def media_matriz(matriz):
    """Funcao que, dado uma matriz de inteiros nao vazia,
    retorne a media de todos os numeros da matriz com uma
    precisao de duas casas decimais:
    list[list] -> float"""
    numero_de_linhas=len(matriz)
    numero_de_colunas=len(matriz[0])
    qnt_elementos=numero_de_linhas*numero_de_colunas
    soma=0
    for linhas in matriz:
        for aij in linhas:
            soma+=aij
    media=soma/qnt_elementos
    return round(media,2)