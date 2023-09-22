def melhor_volta(matriz):
    """Retorne de quem foi a melhor volta da prova, o melhor tempo e em que volta"""
    tempo=(min(matriz))
    for x in range(6):
        for y in range(10):
            if matriz[x][y] < tempo[1]:
                tempo = (x+1,matriz[x][y],y+1)
    return tempo