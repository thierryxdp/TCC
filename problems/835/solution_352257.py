def melhor_volta(matriz):
    '''Dada 10 voltas de uma corrida de Kart para cada 6 corredores, transformo uma matriz 6 x 10 e calculo
de quem foi a melhor volta da prova contendo seu tempo e em qual volta.
lista -> tupla'''
    menor_tp = volta = campeao = 1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], menor_tp) == matriz[v][t]:
                menor_tp = min(matriz[v][t], menor_tp)
                campeao = v + 1
                volta = t + 1

    return campeao, menor_tp, volta