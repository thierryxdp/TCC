def pontos_por_time(x):
    time1=x[0][0]
    time2=x[0][1]
    gols_time1_ida=x[0][2][0]
    gols_time2_ida=x[0][2][1]
    gols_time2_volta=x[1][2][0]
    gols_time1_volta=x[1][2][1]
    pontos_time1=()
    pontos_time2=()
    if int(gols_time1_ida)>int(gols_time2_ida):
        pontos_time1=pontos_time1+(3,)
        pontos_time2=pontos_time2+(0,)
    if int(gols_time1_ida)<int(gols_time2_ida):
        pontos_time2=pontos_time2+(3,)
        pontos_time1=pontos_time1+(0,)
    if int(gols_time1_ida)==int(gols_time2_ida):
        pontos_time1=pontos_time1+(1,)
        pontos_time2=pontos_time2+(1,)
    if int(gols_time1_volta)>int(gols_time2_volta):
        pontos_time1=pontos_time1+(3,)
        pontos_time2=pontos_time2+(0,)
    if int(gols_time1_volta)<int(gols_time2_volta):
        pontos_time2=pontos_time2+(3,)
        pontos_time1=pontos_time1+(0,) 
    if int(gols_time1_volta)==int(gols_time2_volta):
        pontos_time1=pontos_time1+(1,)
        pontos_time2=pontos_time2+(1,)
    total1=int(pontos_time1[0])+int(pontos_time1[1])
    total2=int(pontos_time2[0])+int(pontos_time2[1])
    return {time1:total1,time2:total2}