def media_matriz(matriz):
    """
    Dada uma matriz, calcula a média dela com duas casas decimais de precisão
    list -> float
    """

    s = []
    l = []

    for i in range(len(matriz)):
        s.append(sum(matriz[i]))
        l.append(len(matriz[i]))

    
    return round((sum(s)/sum(l)), 2)