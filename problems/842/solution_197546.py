def pontos_por_time(jogos):
    if jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        resultado={jogos[0][0]:6,jogos[0][1]:0}
    elif jogos[0][2][0]<jogos[0][2][1] and jogos[1][2][1]<jogos[1][2][0]:
            resultado={jogos[0][1]:6,jogos[0][0]:0}
    elif jogos[0][2][0]==jogos[0][2][1] and jogos[1][2][1]==jogos[1][2][0]:
                resultado={jogos[0][0]:2,jogos[0][1]:2}
    elif jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]<jogos[1][2][0]:
        resultado={jogos[0][0]:3,jogos[0][1]:3}
    elif jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]==jogos[1][2][0]:
        resultado={jogos[0][0]:4,jogos[0][1]:1}
    elif jogos[0][2][0]==jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        resultado={jogos[0][0]:4,jogos[0][1]:1}
    elif jogos[0][2][0]==jogos[0][2][1] and jogos[1][2][1]<jogos[1][2][0]:
        resultado={jogos[0][1]:4,jogos[0][0]:1}
    elif jogos[0][2][0]<jogos[0][2][1] and jogos[1][2][1]==jogos[1][2][0]:
        resultado={jogos[0][1]:4,jogos[0][0]:1}
    elif jogos[0][2][0]<jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        resultado={jogos[0][0]:3,jogos[0][1]:3}
    return resultado#Start your python function here