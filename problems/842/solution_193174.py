def pontos_por_time(lista):
    '''list->dict'''
    time1=lista[0][0]
    time2=lista[0][1]
    goli=lista[0][2]
    golv=lista[1][2]
    if goli[0]>goli[1]:
        p1=3
        p2=0
    if goli[0]<goli[1]:
        p1=0
        p2=3
    if goli[0]==goli[1]:
        p1=1
        p2=1
    if golv[0]>golv[1]:
        p2=p2+3
    if golv[0]<golv[1]:
        p1=p1+3
    if golv[0]==golv[1]:
        p1=p1+1
        p2=p2+1
    return {time1:p1,time2:p2}