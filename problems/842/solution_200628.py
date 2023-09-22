def pontos_por_time (timesGols):
    """dada uma lista, contendo outras duas listas, sendo os primeiros 2 elementos dessas listas;
    os times e o terceiro elemento uma lista contendo os gols da rodada respectivamente,
    retorna um dicionario cujos mapeamentos são o nome do time e o total de pontos na fase
    list --> dict"""
    time1=timesGols[0][0]
    time2=timesGols[0][1]
    gols_Time1_Rodada1=timesGols[0][2][0]
    gols_Time2_Rodada1=timesGols[0][2][1]
    gols_Time1_Rodada2=timesGols[1][2][1]
    gols_Time2_Rodada2=timesGols[1][2][0]
    pontos_Time1=0
    pontos_Time2=0
    if gols_Time1_Rodada1>gols_Time2_Rodada1:
        pontos_Time1=pontos_Time1+3
    elif gols_Time1_Rodada1<gols_Time2_Rodada1:
        pontos_Time2=pontos_Time2+3
    else:
        pontos_Time1=pontos_Time1+1
        pontos_Time2=pontos_Time2+1
    if gols_Time1_Rodada2>gols_Time2_Rodada2:
        pontos_Time1=pontos_Time1+3
    elif gols_Time1_Rodada2<gols_Time2_Rodada2:
        pontos_Time2=pontos_Time2+3
    else:
        pontos_Time1=pontos_Time1+1
        pontos_Time2=pontos_Time2+1
    return {time1:pontos_Time1,time2:pontos_Time2}