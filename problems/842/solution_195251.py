def pontos_por_time(jogos):
    time1= 0
    time2= 0
    if jogos[0][2][0]>jogos[0][2][1]:
        time1 += 3
        
    elif jogos[0][2][0]<jogos[0][2][1]:
        time2 += 3
        
    elif jogos[0][2][0]==jogos[0][2][1]:
        time1 += 1
        time2 += 1

    if jogos[1][2][0]>jogos[1][2][1]:
        time2 += 3     

    elif jogos[1][2][0]<jogos[1][2][1]:
        time1 += 3

    elif jogos[1][2][0]==jogos[1][2][1]:
        time1 += 1
        time2 += 1

    dic={jogos[0][0]:time1, jogos[0][1]:time2}
    return dic