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
	if gols_ida_time1 > gols_ida_time2:
        pontos_time1=3
        pontos_time2=0
    if gols_ida_time1 < gols_ida_time2:
		pontos_time2=3
        pontos_time1=0
    if gols_ida_time1==gols_ida_time2:
        pontos_time1=1
        pontos_time2=1
    if gols_volta_time1 > gols_volta_time2:
        pontos_time1_v=3
        pontos_time2_v=0
    if gols_volta_time1 < gols_volta_time2:
        pontos_time2_v=3
        pontos_time1_v=0
    if gols_volta_time1 == gols_volta_time2:
        pontos_time1_v=1
        pontos_time2_v=1
    resultado1=pontos_time1+pontos_time1_v
    resultado2=pontos_time2+pontos_time2_v
    return {'time1_ida':resultado1,'time2_ida':resultado2}