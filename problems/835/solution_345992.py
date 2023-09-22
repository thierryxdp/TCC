def melhor_volta(matriz):
    """
    Dada 10 voltas de uma corrida de Kart para cada 6 corredores, transforma uma matriz 6 x 10 e calcula
    de quem foi a melhor volta da prova contendo seu tempo e em qual volta.
    :param matriz:
    :return:
    """
    vencedor = 0
    menor_tempo = 0
    volta = 0
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v]) in matriz[v]:
                menor_tempo = min(matriz[v])
                volta =  matriz[v].index(menor_tempo)
                vencedor =  matriz.index(matriz[v])

    return vencedor, menor_tempo, volta