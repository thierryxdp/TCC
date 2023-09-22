def melhor_volta(matriz):
    """ retorna uma tup que informa de quem foi a melhor
    volta da prova, qual tempo e em que volta
    list -> tup"""
    corredor = 0
    melhorvolta = matriz[0].index(min(matriz[0]))
    for i in range(1, len(matriz)):
        m = min(matriz[i])
        if (m < matriz[corredor][melhorvolta]):
            corredor = i
            melhorvolta = matriz[i].index(m)
    return (corredor + 1, matriz[corredor][melhorvolta], melhorvolta + 1)