def pontos_por_time(t1,t2):
    t1=pontos_por_time[3:0]+pontos_por_time[6:1]
    t2=pontos_por_time[3:0]+pontos_por_time[6:1]
    if t1>t2:
        return {t1,6}