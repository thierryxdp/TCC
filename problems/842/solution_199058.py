def pontos_por_time(lista):
    listaA, listaB = lista
    time1=listaA[0]
    time2=listaA[1]
    tabela = {time1:0,time2:0}
    placar1time1,placar1time2 = listaA[2]
    placar2time1,placar2time2 = listaB[2]
    if placar1time1 > placar1time2:
        if placar2time1 > placar2time2:
            tabela[str(time1)] = 6
        elif placar2time1 == placar2time2:
            tabela[str(time1)] = 4
            tabela[str(time2)] = 1
        else:
            tabela[str(time1)] = 3
            tabela[str(time2)] = 3
    elif placar1time1 == placar1time2:
            if placar2time1 > placar2time2:
                tabela[str(time1] = 4
                tabela[str(time2)] = 1
            elif placar2time1 < placar2time2:
                tabela[str(time1)] = 1
                tabela[str(time2)] = 4 
            else:
                tabela[str(time1)] = 2
                tabela[str(time2)] = 2
    else:
        if placar2time1 > placar2time2:
            tabela[str(time1)] = 3
            tabela[str(time2)] = 3
        elif placar2time1 == placar2time2:
            tabela[str(time1)] = 1
            tabela[str(time2)] = 4
        else:
            tabela[str(time2)] = 6
    return tabela