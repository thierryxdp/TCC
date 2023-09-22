def pontos_por_time(L1,L2):
    gols_ida=L1[2]
    gols_volta=L2[2]
    time1=L1[0]
    time2=L1[1]
    if gols_ida[0]>gols_ida[1]:
        time1_ida=3
    if gols_ida[0]<gols_ida[1]:
        time2_ida=3
    if gols_ida[0]==gols_ida[1]:
        time1_ida=1
        time2_ida=1
    if gols_volta[0]>gols_volta[1]:
        time2_volta=3
    if gols_volta[0]<gols_volta[1]:
        time1_volta=3
    if gols_volta[0]==gols_volta[1]:
        time1_volta=1
        time2_volta=1
    return {time1:time1_ida+time1_volta,\
            time2:time2_ida+time2_volta}