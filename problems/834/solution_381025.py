def media_matriz (matriz):
    """Retorna cada elemento da matriz de entrada divido ao meio"""
    soma=[]
    for lista in matriz:
        for elemento in lista:
            soma += elemento
            geral = sum(soma)
            metade = geral/2
    return metade