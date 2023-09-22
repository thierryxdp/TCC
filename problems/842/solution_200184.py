def pontos_por_times(lista):
    
    pontos_time1=0
    pontos_time2=0
    
    if lista[0][2][0]>lista[0][2][1]:
        pontos_time1=pontos_time1+3
    if lista[0][2][0]==lista[0][2][1]:
        pontos_time1=pontos_time1+1
        pontos_time2=pontos_time2+1
    if lista[0][2][0]<lista[0][2][1]:
        pontos_time2=pontos_time2+3
        
    elif lista[1][2][0]<lista[1][2][1]:
        pontos_time1=pontos_time1+3
    if lista[1][2][0]==lista[1][2][1]:
        pontos_time1=pontos_time1+1
        pontos_time2=pontos_time2+1
    if lista[1][2][0]>lista[1][2][1]:
        pontos_time2=pontos_time2+3
        
    tabela= {lista[0][0]:pontos_time1, lista[0][1]:pontos_time2}
    
     return tabela