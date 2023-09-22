def melhor_volta(matriz):
    """Dada a matriz com as voltas dos corredores
    retorna o melhor colocado."""
    corred = 0
    tupla = ()
    minimo = []
    corredores = len(matriz)
    voltas = len(corredores)
    for i in range (corredores):
        for j in range(voltas):
            minimo += [min(matriz[i][:])]
            if min(minimo) in matriz[i]:
                corred = i +1
                indice = matriz[i].index(min(minimo))
    return corred,min(minimo),indice