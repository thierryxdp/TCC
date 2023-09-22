def media_matriz(matriz):
    """A funcao media_matriz recebe como entrada somente uma matriz, e retorna
    a media de todos os elementos dela, com precisao de duas casas decimais.
    entrada: int -> return int"""
    pos = 0
    soma = 0
    for pos in range(len(matriz)):
        soma += sum(matriz[pos],)/(len(matriz[pos],) * len(matriz))
    return round(soma,2)