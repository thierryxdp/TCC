def pontos_por_time(lista):
    time1=lista[0][0]
    time2=lista[0][1]
    pontostime1=0
    pontostime2=0
    
    if lista[0][2][0] ==lista[0][2][1]:
        pontostime1=pontostime1+1
        pontostime2=pontostime2+1
    
    if lista[0][2][0] >lista[0][2][1]:
        pontostime1=pontostime1+3
        
    if lista[0][2][0] <lista[0][2][1]:
        pontostime2=pontostime2+3
        
    if lista[1][2][0] ==lista[1][2][1]:
        pontostime1=pontostime1+1
        pontostime2=pontostime2+1
        
    if lista[1][2][0] >lista[1][2][1]:
        pontostime2=pontostime2+3
        
    if lista[1][2][0] <lista[1][2][1]:
        pontostime1=pontostime1+3
        
    dicio = {time1:pontostime1,time2:pontostime2}
    return dicio