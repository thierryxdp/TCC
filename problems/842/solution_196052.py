def pontos_por_time(lista1,lista2):
    jogo1 = [lista1[0], lista1[1],[lista1[2][0], lista1[2][1]]
    jogo2 = [lista2[0], lista2[1],[lista2[2][0], lista2[2][1]]
    time1 = lista1[0]
    time2 = lista2[0]
    
    if lista1[2][0] > lista1[2][1] and lista2[2][0] < lista2[2][1]:
        return {time1:6, time2:0}
    elif lista1[2][0] < lista1[2][1] and lista2[2][0] > lista2[2][1]:
        return {time1:0, time2:6}
    elif lista1[2][0] > lista1[2][1] and lista2[2][0] > lista2[2][1]:
        return {time1:3, time2:3}
    elif lista1[2][0] < lista1[2][1] and lista2[2][0] < lista2[2][1]:
        return {time1:3, time2:3}
    elif  lista1[2][0] == lista1[2][1] and lista2[2][0] < lista2[2][1]:
        return {time1:4, time2:1}
    elif  lista1[2][0] > lista1[2][1] and lista2[2][0] == lista2[2][1]:
        return {time1:1, time2:4}
    else:
        return {time1:1, time2:1}