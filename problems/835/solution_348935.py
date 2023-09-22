def melhor_volta(matriz):
    """Função que recebe uma matriz 6x10 (10 voltas na pista de kart para cada 6 corredores)
       com os tempos em segundos dos corredores em cada volta e retorna uma tupla contendo de
       quem foi a melhor volta da prova, com qual tempo e em que volta.
       list->tuple"""
    menor_tempo = 1000
    volta = 1000
    melhor_volta = 1000
    for v in range(0,len(matriz)):
        for t in range(0,len(matriz[v])):
            if min (matriz[v][t],menor_tempo)== matriz[v][t]:
                menor_tempo = min(matriz[v][t],menor_tempo)
                melhor_volta = v + 1
                volta = t + 1
    return vencedor,menor_tempo,volta