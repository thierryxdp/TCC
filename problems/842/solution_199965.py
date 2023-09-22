def pontos_por_time(lista):
    '''Recebe uma lista de dois elementos com informações do número de gols
    em dois jogos de futebol entre dois times (ida e volta).
    list -> dict'''
    dados = {'time1': lista[0][0],
             'time2': lista[1][0],
             'gols_time1_primeiro_tempo': lista[0][2][0],
             'gols_time1_segundo_tempo': lista[1][2][1],
             'gols_time2_primeiro_tempo': lista[0][2][1],
             'gols_time2_segundo_tempo': lista[1][2][0],}

    pontos1_time1 = 0
    pontos2_time1 = 0
    pontos1_time2 = 0
    pontos2_time2 = 0

    if lista[0][2][0] > lista[0][2][1] and lista[1][2][1] > lista[1][2][0]:
        pontos1_time1 += 3
        pontos2_time1 += 3
    elif lista[0][2][0] < lista[0][2][1] and lista[1][2][1] < lista[1][2][0]:
        pontos1_time2 += 3
        pontos2_time2 += 3

    elif lista[0][2][0] > lista[0][2][1] and lista[1][2][1] == lista[1][2][0]:
        pontos1_time1 += 4

    elif lista[0][2][0] < lista[0][2][1] and lista[1][2][1] == lista[1][2][0]:
        pontos1_time2 += 4

    elif lista[0][2][0] == lista[0][2][1] and lista[1][2][1] > lista[1][2][0]:
        pontos2_time1 += 4

    elif lista[0][2][0] == lista[0][2][1] and lista[1][2][1] < lista[1][2][0]:
        pontos2_time2 += 4
    return dados["time1"], pontos1_time1+pontos2_time1, dados["time2"], pontos1_time2 + pontos2_time2