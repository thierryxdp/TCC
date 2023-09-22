def pontos_por_time(lista):
    '''retorna um dicionario de acordo com numeros de pontos de cada time, list=>dic'''
    ida=lista[0]
    volta=lista[1]
    time1=ida[0]
    time2=ida[1]
    time1=volta[0]
    time2=volta[1]
    gols_ida=ida[2]
    gols_volta=volta[2]
    gols_ida_time1=gols_ida[0]
    gols_ida_time2=gols_ida[1]
    gols_volta_time1=gols_volta[0]
    gols_volta_time2=gols_volta[1]
    if (gols_ida[0]<gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]>gols_ida[1] and gols_volta[0]<gols_volta[1]):
        return {time1:3,time2:3}
    elif (gols_ida[0]==gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]==gols_ida[1] and gols_volta[0]>gols_volta[1]):
        return {time1:4,time2:1}
    elif (gols_ida[0]==gols_ida[1] and gols_volta[0]<gols_volta[1]) or (gols_ida[0]==gols_ida[1] and gols_volta[0]<gols_volta[1]):
        return {time:1,time2:4}
    elif (gols_ida[0]>gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]>gols_ida[1] and gols_volta[0]>gols_volta[1]):
        return {time1:6,time2:0}
    elif (gols_ida[0]<gols_ida[1] and gols_volta[0]<gols_volta[1]) or (gols_ida[0]<gols_ida[1] and gols_volta[0]<gols_volta[1]):
        return {time1:0.time2:6}
    else:
        return {time1:2,time1:2}