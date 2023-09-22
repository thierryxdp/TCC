def pontos_por_time (a):
    Jogo1 = a[0]
    Jogo2 = a[1]
    TimeA = Jogo1[0]
    TimeB = Jogo1[1]
    Time1 = TimeA
    Time2 = TimeB
    placar1 = Jogo1[2]
    placar2 = Jogo2[2]
    vitoriaA1 = placar1[0] > placar1[1]
    vitoriaA2 = placar2[0] < placar2[1]
    vitoriaB1 = placar1[0] < placar1[1]
    vitoriaB2 = placar2[0] > placar2[1]
    empate1 = placar1[0] == placar1[1]
    empate2 = placar2[0] == placar2[1]
    if vitoriaA1 and vitoriaA2 == True:
        return ((Time1) + " :" " 6", (Time2) + " :" + " 0")
    elif vitoriaA1 and empate2 == True: 
        return ((Time1) + " :" " 4", (Time2) + " :" + " 1")
    elif vitoriaA2 and empate1 == True: 
        return ((Time1) + " :" " 1", (Time2) + " :" + " 4")
    elif vitoriaB1 and vitoriaB2 == True:
        return ((Time1) + " :" " 0", (Time2) + " :" + " 6")
    else:
        return ((Time1) + " :" " 2", (Time2) + " :" + " 2")