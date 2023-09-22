def pontos_por_time(lista): # FAZER A IDENTIFICAÇÃO #
    time1=lista[0][0]
    time2=lista[0][1]
    pontos_time_1=0
    pontos_time_2=0
    gols_time1_p1=lista[0][2][0]
    gols_time1_p2=lista[1][2][1]
    gols_time2_p1=lista[0][2][1]
    gols_time2_p2=lista[1][2][0]
    if gols_time1_p1>gols_time2_p1:
        pontos_time_1+=3
    if gols_time2_p1>gols_time1_p1:
        pontos_time_2+=3
    if gols_time2_p1==gols_time1_p1:
        pontos_time2+=1
        pontos_time1+=1
    if gols_time1_p2>gols_time2_p2:
        pontos_time1+=3
    if gols_time2_p2>gols_time1_p2:
        pontos_time_2+=3
    if gols_time2_p2==gols_time1_p2:
        pontos_time_2+=1
        pontos_time_1+=1
    return {time1:pontos_time_1,time2:pontos_time_2}