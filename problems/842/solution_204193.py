def pontos_por_time(lista):
    """doc"""
    gol_ida_time1=lista[0][2][0]
    gol_volta_time1=lista[1][2][1]
    gol_ida_time2=lista[0][2][1]
    gol_volta_time2=lista[1][2][0]
    
    a1=gol_ida_time1
    a2=gol_volta_time1
    b1=gol_ida_time2
    b2=gol_volta_time2
    
    if a1 > b1:
        a1=3
        b1=0
    elif a1==b1:
        a1=1
        b1=1
    else:
        a1=0
        b1=3
        
    if a2>b2:
        a2=3
        b2=0
    elif a2==b2:
        a2=1
        b2=1
    else:
        a2=0
        b2=3
    
    return {lista[0][0]:a1+a2,lista[0][1]:b1+b2}