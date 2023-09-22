def pontos_por_time(resultados):
    placa_ida=resultados[0]
    placar_ida=placa_ida[-1]
    placa_volta=resultados[-1]
    placar_volta=placa_volta[-1]
    placares=placar_ida[:]+placar_volta[:]

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

    return {jogo_ida[0]:pontos_time1,jogo_volta[1]:pontos_time2}