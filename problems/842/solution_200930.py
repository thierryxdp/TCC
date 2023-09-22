def pontos_por_time(L):
    '''funcao que dado uma lista contendo o
numero de gols em dois jogos de futebol entre
dois times (jogo de ida e jogo de volta ), no seguinte formato:
[[time1,time2,[gol1,gol2]],[time2,time1,[gol2,gol1]]].
Retorna um dicionario contendo o nome do time com o respectivo
total de pontos; list -> dict'''
    if L[0][2][0] > L[0][2][1]:
        time1 = 3.0
        time2 = 0.0
    elif L[0][2][0] < L[0][2][1]:
        time2 = 3.0
        time1 = 0.0
    else:
        time1 = 1.0
        time2 = 1.0
    if L[1][2][1] > L[1][2][0]:
        Time1 = 3.0
        Time2 = 0.0
    elif L[1][2][1] < L[1][2][0]:
        Time2 = 3.0
        Time1 = 0.0
    else:
        Time1 = 1.0
        Time1 = 1.0
    #Total de pontos
    TP1 = time1 + Time1
    TP2 = time2 + Time2
    return {L[0][0]:TP1,L[0][1]:TP2}