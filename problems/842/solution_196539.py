def pontos_por_time(lista):
    lista = [lista1,lista2]
    lista1 = ([time1,time2,[placar1,placar2]])
    lista2 = [time2,time1,[placar3,placar4]]
    placar1 = lista1[2][0]
    placar2 = lista1[2][1]
    placar3 = lista2[2][0]
    placar4 = lista2[2][1]
    time1 = lista1[0]
    time2 = lista2[0]
    
    if (placar1 > placar2) and (placar3 < placar4):
        return {time1:6, time2:0}
    elif (placar1 < placar2) and (placar3 > placar4):
        return {time1:0, time2:6}
    elif (placar1 > placar2) and (placar3 > placar4):
        return {time1:3, time2:3}
    elif (placar1 < placar2) and (placar3 < placar4):
        return {time1:3, time2:3}
    elif  (placar1 == placar2) and (placar3 < placar4):
        return {time1:4, time2:1}
    elif  (placar1 < placar2) and (placar3 == placar4):
        return {time1:1, time2:4}
    else:
        return {time1:1, time2:1}