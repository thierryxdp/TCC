def media_matriz(matriz):
    """Funcao que dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz (com duas casas decimais);
    lista(lista) -> float"""

    numero = 0
    qtd = 0
    
    nlin = len(matriz)
    ncol = len(matriz[0])

    for i in range(nlin):
        for j in range(ncol):
            numero = numero + matriz[i][j]
            qtd = qtd + 1
    return round((numero/qtd),2)