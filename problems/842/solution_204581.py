def pontos_por_time(lista)
    '''Função que retornará quantos pontos cada time obteve com os 2 jogos'''

    lista_primeirojogo = lista[0]
    lista_segundojogo = lista[1]
    time_um = lista_primeirojogo[0]
    time_dois = lista_primeirojogo[1]
    placar_um = lista_primeirojogo[2]
    placar_dois = lista_segundojogo[2]
    pontos_time_um = 0
    pontos_time_dois = 0

    if len(lista) == 2:
        if (int(placar_um[0]) > int(placar_um[1])):
            pontos_time_um += 3
        elif (int(placar_um[0]) < int(placar_um[1])):
            pontos_time_dois += 3
        elif (int(placar_um[0]) == int(placar_um[1])):
            pontos_time_um += 1
            pontos_time_dois += 1

        if (int(placar_dois[0]) > int(placar_dois[1])):
            pontos_time_dois += 3
        elif (int(placar_dois[0]) < int(placar_dois[1])):
            pontos_time_um += 3
        elif (int(placar_dois[0]) == int(placar_dois[1])):
            pontos_time_um += 1
            pontos_time_dois += 1
    return {time_um:pontos_time_um,time_dois:pontos_time_dois}