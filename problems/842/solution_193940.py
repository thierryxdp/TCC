def pontos_por_time(lista):
    '''tendo como entrada os dados dos jogos de ida e volta entre 2 times, retorna um dicionário com os pontos conquistados por cada um7
    list-->dictionary'''
    time_1=lista[0][0]
    time_2=lista[0][1]
    gols_1=lista[0][2]
    gols_2=lista[1][2]
    if gols_1[0]>gols_1[1]:
        P1=3
        P2=0
    elif gols_1[0]<gols_1[1]:
        P1=0
        P2=3
    elif gols_1[0]==gols_1[1]:
        P1=1
        P2=1
    if gols_2[0]>gols_2[1]:
        P2=P2+3
    elif gols_2[0]<gols_2[1]:
        P1=P1+3
    elif gols_2[0]==gols_2[1]:
        P1=P1+1
        P2=P2+1
    return {time_1:P1,time_2:P2}