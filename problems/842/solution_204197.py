def pontos_por_time(time1,time2,gols1,gols2,time2,time1,gols22,gols12):
    """"""
    tabela = {}
    if gols1>gols2:
        pontos1=3
        pontos2=0
    elif gols1==gols2:
        pontos1=1
        pontos2=1
    else:
        pontos2=3
        pontos1=0