def pontos_por_time(camp)
    pontos_time1=0
    pontos_time2=0
    placar_ida=camp[0][2]
    placar_volta=camp[1][2]
    nome_time1=camp[0][0]
    nome_time2=camp[0][1]
    if placar_ida[0]>placar_ida[1]:
        pontos_time1=3
    if placar_volta[1]>placar_volta[0]:
        pontos_time1+=3
    if placar_ida[1]>placar_ida[0]:
        pontos_time2=3
    if placar_volta[0]>placar_volta[1]:
        pontos_time2+=3
    if placar_ida[0]==placar_ida[1]:
        pontos_time1+=1
        pontos_time2+=1
    if placar_volta[0]==placar_volta[1]:
        pontos_time1+=1
        pontos_time2+=1
    return {nome_time1:pontos_time1,nome_time2:pontos_time2}