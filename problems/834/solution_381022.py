def media_matriz (matriz):
    """Retorna cada elemento da matriz de entrada divido ao meio"""
    metade=[]
    for lista in matriz:
        for elemento in lista:
            meio = round(elemento/2,2)
            metade = metade + meio
    return metade