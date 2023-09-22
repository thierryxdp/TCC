def pontos_por_time(lista):
    ''' '''
    ida=lista[0]
    volta=lista[1]
    time1_ida=ida[0]
    time2_ida=ida[1]
    time1_volta=volta[0]
    time2_volta=volta[1]
    gols_ida=ida[2]
    gols_volta=volta[2]

    if time1_ida==time1_volta:
        time1=time1_ida
        time2=time2_ida
        if (gols_ida[0]<gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]>gols_ida[1] and gols_volta[0]<gols_volta[1]):
            return {time1:3,time2:3}
        elif (gols_ida[0]==gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]==gols_ida[1] and gols_volta[0]>gols_volta[1]):
            return {time1:4,time2:1}
        elif (gols_ida[0]==gols_ida[1] and gols_volta[0]<gols_volta[1]) or (gols_ida[0]==gols_ida[1] and gols_volta[0]<gols_volta[1]):
            return {time:1,time2:4}
        elif (gols_ida[0]>gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]>gols_ida[1] and gols_volta[0]>gols_volta[1]):
            return {time1:6,time2:0}
        elif (gols_ida[0]<gols_ida[1] and gols_volta[0]<gols_volta[1]) or (gols_ida[0]<gols_ida[1] and gols_volta[0]<gols_volta[1]):
            return {time1:0,time2:6}
        else:
            return {time1:2,time2:2}
    else:
        lista=[ida,[volta[1],volta[0],[volta[2][1],volta[2][0]]]]
        ida=lista[0]
        volta=lista[1]
        time1_ida=ida[0]
        time2_ida=ida[1]
        time1_volta=volta[0]
        time2_volta=volta[1]
        gols_ida=ida[2]
        gols_volta=volta[2]
        time1=time1_ida
        time2=time2_ida
                    
        if (gols_ida[0]<gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]>gols_ida[1] and gols_volta[0]<gols_volta[1]):
            return {time1:3,time2:3}
        elif (gols_ida[0]==gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]==gols_ida[1] and gols_volta[0]>gols_volta[1]):
            return {time1:4,time2:1}
        elif (gols_ida[0]==gols_ida[1] and gols_volta[0]<gols_volta[1]) or (gols_ida[0]==gols_ida[1] and gols_volta[0]<gols_volta[1]):
            return {time:1,time2:4}
        elif (gols_ida[0]>gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]>gols_ida[1] and gols_volta[0]>gols_volta[1]):
            return {time1:6,time2:0}
        elif (gols_ida[0]<gols_ida[1] and gols_volta[0]<gols_volta[1]) or (gols_ida[0]<gols_ida[1] and gols_volta[0]<gols_volta[1]):
            return {time1:0,time2:6}
        else:
            return {time1:2,time2:2}