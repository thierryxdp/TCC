def pontos_por_time(lista): # FAZER A IDENTIFICAÇÃO #
    nome1=lista[0][0]
    nome2=lista[0][1]
    pontos_time1_p1=0
    pontos_time2_p2=0
    time1_p1=lista[0][2][0]
    time1_p2=lista[1][2][1]
    time2_p1=lista[0][2][1]
    time2_p2=lista[1][2][0]
    if time1_p1>time2_p1:
        pontos_time1_p1=+3   
    if time1_p1<time2_p1:
        pontos_time2_p1=+3     
    if time2_p2>time1_p2:
        pontos_time2_p2=+3    
    if time1_p2>time2_p2:
        pontos_time1_p2=+3    
    if time1_p1==time2_p1:
        pontos_time1_p1+=1
        pontos_time2_p1+=1
    if time2_p2==time1_p2:
        pontos_time1_p2+=1
        pontos_time2_p2+=1 
    return {nome1:pontos_time_p1,nome2:pontos_time_p2}