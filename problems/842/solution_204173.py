def pontos_por_time (a, b):
    Time = a[0]
    Time1 = Time[0]
    Time2 = Time[1]
    placar1 = a[1]
    placar2 = b[1]
    vitoriaA1 = placar1[0] > placar1[1]
    vitoriaA2 = placar2[0] < placar2[1]
    vitoriaB1 = placar1[0] < placar1[1]
    vitoriaB2 = placar2[0] > placar2[1]
    empate1 = placar1[0] == placar1[1]
    empate2 = placar2[0] == placar2[1]
    if vitoriaA1 and vitoriaA2 == True:
        return ((Time1) + " :" " 6", (Time2) + " :" + " 0")
    else: 
        return False