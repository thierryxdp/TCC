def pontos_por_time[[lista1],[lista2]]:
    '''dada uma lista formada por duas outras listas contendo o numero de gols de cada time em dois jogos, no formato: [<time1>, <time2>, [<gols_time1>, <gols_time2>]], retorna um dicionario com os pontos de cada time nessa fase; lista -> dicionario'''
    if pontos_por_time[0][2][0] > pontos_por_time[0][2][1]:
        return vitoria1_1
    elif pontos_por_time[0][2][0] < pontos_por_time[0][2][1]:
        return vitoria1_2
    elif pontos_por_time[0][2][0] == pontos_por_time[0][2][1]:
        return empate1
    elif pontos_por_time[1][2][0] < pontos_por_time[1][2][1]:
        return vitoria2_1
    elif pontos_por_time[1][2][0] > pontos_por_time[1][2][1]:
        return vitoria2_2
    elif pontos_por_time[1][2][0] == pontos_por_time[1][2][1]:
        return empate2
    time1 = pontos_por_time[0][0]
    time2 = pontos_por_time[0][1]
    fase = {time1:0,time2:0}
    vitoria1_1 = fase[time1] =+ 3
    vitoria1_2 = fase[time2] =+ 3
    vitoria2_1 = fase[time1] =+ 3
    vitoria2_2 = fase[time2] =+ 3
    empate1 = fase[time1] =+ 1
    empate2 = fase[time2] =+ 1