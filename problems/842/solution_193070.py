def pontos_por_time (lista):
    time1 = lista[0]
    time2 = lista[1]
    ponto1 = lista[2]
    ponto2 = lista[3]
    lista = [time1,time2,[ponto1,ponto2]]

    if ponto1 > ponto2:
        pontos1 = + 3
    elif ponto2 > ponto1:
        pontos2 = + 3
    else:
        pontos1 = +1
        pontos2 = +1
    return {time1 : pontos1, time2 : pontos2}