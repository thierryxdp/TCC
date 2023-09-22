def pontos_por_time(listaResultados):
    
    time1 = listaResultados[0][0]
    time2 = listaResultados[0][1]
    pontos_time1 = 0
    pontos_time2 = 0

    if listaResultados[0][2][0] > listaResultados[0][2][1]:
        if listaResultados[0][0] == time1:
            pontos_time1 += 3
        else:
            pontos_time2 += 3
    elif listaResultados[0][2][0] < listaResultados[0][2][1]:
        if listaResultados[0][0] == time1:
            pontos_time1 += 3
        else:
            pontos_time2 += 3
    else:
        pontos_time1 += 1
        pontos_time2 += 1

    if listaResultados[1][2][0] > listaResultados[1][2][1]:
        if listaResultados[1][0] == time2:
            pontos_time2 += 3
        else:
            pontos_time1 += 3
    elif listaResultados[1][2][0] < listaResultados[1][2][1]:
        if listaResultados[1][0] == time2:
            pontos_time2 += 3
        else:
            pontos_time1 += 3
    else:
        pontos_time1 += 1
        pontos_time2 += 1
    dicionario = {time1: pontos_time1, time2 : pontos_time2}
    return dicionario