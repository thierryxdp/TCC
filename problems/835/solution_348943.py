def melhor_volta(matriz):
    """Função que recebe uma matriz 6x10 (10 voltas na pista de kart para cada 6 corredores)
       com os tempos em segundos dos corredores em cada volta e retorna uma tupla contendo de
       quem foi a melhor volta da prova, com qual tempo e em que volta.
       list->tuple"""
    tempo = 1000
    volta = 1000
    melhor_volta = 1000
    for voltas in range(0,len(matriz)):
        for tempos in range(0,len(matriz[voltas])):
            if matriz[voltas][tempos] == min (matriz[voltas][tempos],tempo):
                tempo = min(matriz[voltas][tempos],tempo)
                melhor_volta = voltas + 1
                volta = tempos + 1
    return melhor_volta,tempo,volta