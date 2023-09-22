def pontos_por_time(lista1):
    '''retorna o número total de pontos conquistados pelos 
    times;'''
    
    time1=lista[0][0]
    time2=lista[0][1]
    gtime1i=lista[0][2][0]
    gtime2i=lista[0][2][1]
    gtime1v=lista[1][2][1]
    gtime2v=lista[1][2][0]
    ptime1=0
    ptime2=0
    
    if gtime1i>gtime2i:
        ptime1+=3
    if gtime2i>gtime1i:
        ptime2+=3
    if gtime1i==gtime2i:
        ptime1+=1
        ptime2+=1
    if gtime1v>gtime2v:
        ptime1+=3
    if gtime2v>gtime1v:
        ptime2+=3
    if gtime1v==gtime2v:
        ptime1+=1
        ptime2+=1
    return {time1:ptime1, time2:ptime2}