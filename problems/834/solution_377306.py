def media_matriz(matriz):
    """Função que, dada uma matriz de números inteiros
    calcula e retorna a média desses números
    list -> float"""
    if matriz == []:
        return 0
    soma=0
    num=0
    for a in matriz:
        for b in a:
            soma += b
            num += 1
    return round((soma/num), 2)