def melhor_volta(matriz):
    """..."""
    postmat = 0
    menorvolta = []
    
    for posmat in range(len(matriz)):
        for i in range(len(matriz[posmat])):
            x = min(matriz[posmat])
            list.append(menorvolta, x)
        posmat = posmat + 1
    return menorvolta