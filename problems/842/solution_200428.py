def pontos_por_time (lista):
    '''função que retorna um dicionario com os pontos de cada time; 
    list->dicionario'''
    nome1=lista[0][0]
    nome2=lista[0][1]
    time1_p1=lista[0][2][0]
    time1_p2=lista[1][2][1]
    time2_p1=lista[0][2][1]
    time2_p2=lista[1][2][0]
    if time1_p1>time2_p1:
        time1_p1=3
    if time1_p1>time2_p1:
        time2_p1=0    
    if time1_p1<time2_p1:
        time2_p1=3 
    if time1_p1<time2_p1:
        time1_p1=0     
    if time2_p2>time1_p2:
        time2_p2=3
    if time2_p2>time1_p2:
        time1_p2=0    
    if time1_p2>time2_p2:
        time1_p2=3
    if time1_p2>time2_p2:
        time2_p2=0    
    if time1_p1==time2_p1:
        time1_p1==1
    if time1_p1==time2_p1:
        time2_p1==1 
    if time2_p2==time1_p2:
        time1_p2=1
    if time2_p2==time1_p2:
        time2_p2==1
    pontos1= (time1_p1) + (time1_p2)
    pontos2= (time2_p1) + (time2_p2) 
    
    return {nome1:pontos1,nome2:pontos2}