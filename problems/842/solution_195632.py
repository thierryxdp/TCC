def pontos_por_time(placares):
    placa_ida=placares[0]
    placar_ida=placa_ida[-1]
    placa_volta=placares[-1]
    placar_volta=placa_volta[-1]
    placares=placar_ida[:]+placar_volta[:]
    time1=placares[0][0]
    time2=placares[1][0]

    def pontos_time1(placares):
        if placares[0]>placares[1]and placares[3]>placares[2]:
            return 6
        if placares[0]==placares[1]and placares[3]==placares[2]:
            return 2
        if placares[0]<placares[1]and placares[3]<placares[2]:
            return 0
        if(placares[0]>placares[1]or placares[3]>placares[2]) and (placares[0]<placares[1]or placares[3]<placares[2]):
            return 3
        if(placares[0]>placares[1]or placares[3]>placares[2])and (placares[0]==placares[1]or placares[3]==placares[2]):
            return 4
        if(placares[0]==placares[1]or placares[3]==placares[2])and (placares[0]<placares[1]or placares[3]<placares[2]):
            return 1
    def pontos_time2(placares):
        if placares[1]>placares[0]and placares[2]>placares[3]:
            return 6
        if placares[1]==placares[0]and placares[2]==placares[3]:
            return 2
        if placares[1]<placares[0]and placares[2]<placares[3]:
            return 0
        if (placares[1]>placares[0]or placares[2]>placares[3])and (placares[1]<placares[0]or placares[2]<placares[3]):
            return 3
        if (placares[1]>placares[0]or placares[2]>placares[3])and (placares[1]==placares[0]or placares[2]==placares[3]):
            return 4
        if (placares[1]==placares[0]or placares[2]==placares[3])and (placares[1]<placares[0]or placares[2]<placares[3]):
            return 1

    return {time1:pontos_time1,time2:pontos_time2}