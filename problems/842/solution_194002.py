def pontos_por_time (lista1):
    time1 = lista1 [0][0]
    time2 = lista1 [0][1]
    pontotime1 = lista1 [0][2][0]
    pontotime2 = lista1 [0][2][1]
    
    time1_2 = lista1 [1][0]
    time2_2 = lista1 [1][1]
    pontotime1_2 = lista1 [1][2][0]
    pontotime2_2 = lista1 [1][0][1]
    
    if pontotime1 > pontotime2:
        return [time1 : [3,0]]
    if pontotime1_2 < pontotime2_2:
        return [time2 : [3,0]]
    if pontotime1 = pontotime2:
        return [time1 and time2 : [1,1]]