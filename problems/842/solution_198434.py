def pontos_por_time(lista):
    time1 = lista[0][0]
    time2 = lista[0][1]
    dic = {time1: 0, time2: 0}
    
    if lista[0][2][0] > lista[0][2][1]:
        dic[time1] = dic[time1] + 3
    elif lista[0][2][0] = lista[0][2][1]:
        dic[time1] = dic[time1] + 1
        dic[time2] = dic[time2] + 1
    elif lista[1][2][0] < lista[1][2][1]:
        dic[time2] = dic[time2] + 3
    
    if lista[1][2][0] > lista[1][2][1]:
        dic[time1] = dic[time1] + 3
    elif lista[1][2][0] = lista[1][2][1]:
        dic[time1] = dic[time1] + 1
        dic[time2] = dic[time2] + 1
    elif lista[1][2][0] < lista[1][2][1]:
        dic[time2] = dic[time2] + 3
    
    return dic