def melhor_volta(matriz):
    """ retorna uma tup que informa de quem foi a melhor
    volta da prova, qual tempo e em que volta
    list -> tup"""
    corredor = 0
    melhor_volta = matriz[0].indez(min(matriz[0]))
    for i in range(1, len(matriz)):
        m = min(matriz[i]
        if (m < matriz[corredor][melhor_volta]):
            corredor = i
            melhor_volta = corrida[i].index(m)
    return (corredor + 1, matriz[corredor][melhor_volta], melhor_volta + 1)