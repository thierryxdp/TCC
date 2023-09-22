def pontos_por_time(lista):
    """[['time1','time2',[1,0] ,'time 2','time 1',[ida,volta]]] """
    time1_ida=lista[0] [0]
    time2_ida=lista[0] [1]
    gols_ida_time1=lista [0] [2] [0]
    gols_ida_time2=lista [0] [2] [1]
    time1_volta=lista [1] [1]
    time2_volta=lista [1] [0]
    gols_volta_time1=lista [1] [2] [1]
    gols_volta_time2=lista [1] [2] [0]
    return time1_ida, time2_ida, gols_ida_time1, gols_ida_time2, time1_volta,time2_volta,gols_volta_time1,gols_volta_time2