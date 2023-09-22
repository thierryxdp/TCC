def pontos_por_time(jogos):
    time1 = 0
    time2 = 0
    
    if jogos[0][2][0]>jogos[0][2][1]:
        time1 += 3
        time2 += 0
        
    elif jogos[0][2][0]<jogos[0][2][1]:
        time1 += 0
        time2 += 3
        
    elif jogos[0][2][0]==jogos[0][2][1]:
        time1 += 1
        time2 += 1

    elif jogos[1][2][0]>jogos[1][2][1]:
        time2 += 3
        time1 += 0

    elif jogos[1][2][0]<jogos[1][2][1]:
        time2 += 0
        time1 += 3

    elif jogos[1][2][0]==jogos[1][2][1]:
        time2 += 1
        time1 += 1


    return (time1,time2)