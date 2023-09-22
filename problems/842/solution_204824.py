def pontos_por_time (lista):
    '''Função que retornará potuação por time com os 2 jogos'''
    lista_primeirojogo,lista_segundojogo= lista
    time_um,time_dois,placar_um= lista_primeirojogo
    pontos1time1,pontos1time2=placar_um
    timeA,timeB,placar_2= lista_segundojogo
    pontos2time1,pontos2time2=placar_2
    pontos_time_um = 0
    pontos_time_dois = 0

    if len(lista) == 2:
        if (int(pontos1time1) > int(pontos1time2)):
            pontos_time_um += 3
        elif (int(pontos1time1) < int(pontos1time2)):
            pontos_time_dois += 3
        elif (int(pontos1time1) == int(pontos1time2)):
            pontos_time_um += 1
            pontos_time_dois += 1

        if (int(pontos2time1) > int(pontos2time2)):
            pontos_time_dois += 3
        elif (int(pontos2time1) < int(pontos2time2)):
            pontos_time_um += 3
        elif (int(pontos2time1) == int(pontos2time2)):
            pontos_time_um += 1
            pontos_time_dois += 1
    return {time_um:pontos_time_um,time_dois:pontos_time_dois}