def pontos_por_time(lista):
    '''retorna um dicionario com nome do time e seu total de pontos,list->dic'''
    if lista[0][0]==lista[1][0]:
        lista = lista
    else:
        lista=[lista[0],[lista[1][1],lista[1][0],[lista[1][2][1],lista[1][2][0]]]]
    
    gols_ida=lista[0][2]
    gols_volta=lista[1][2]
    time1=lista[0][0]
    time2=lista[1][1]
    
    if (gols_ida[0]<gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]>gols_ida[1] and gols_volta[0]<gols_volta[1]):
        return {time1:3,time2:3}
    elif (gols_ida[0]==gols_ida[1] and gols_volta[0]>gols_volta[1]) or (gols_ida[0]>gols_ida[1] and gols_volta[0]==gols_volta[1]):
        return {time1:4,time2:1}
    elif (gols_ida[0]<gols_ida[1] and gols_volta[0]==gols_volta[1]) or (gols_ida[0]==gols_ida[1] and gols_volta[0]<gols_volta[1]):
        return {time1:1,time2:4}
    elif (gols_ida[0]>gols_ida[1] and gols_volta[0]>gols_volta[1]):
        return {time1:6,time2:0}
    elif (gols_ida[0]<gols_ida[1] and gols_volta[0]<gols_volta[1]):
        return {time1:0,time2:6}
    else:
        return {time1:2,time2:2}