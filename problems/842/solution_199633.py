def pontos_por_time(lista):
    ''' documentação
    list->dict'''
    timeA = lista[0][0]
    timeB = lista[0][1]
    
    goltimeA1 = lista[0][2][0]
    goltimeB1 = lista[0][2][1]
    
    timeA == lista[0][0]
    timeB == lista[1][0]
    
    goltimeA2 = lista[0][2][1]
    goltimeB2 = lista[1][2][0]
    ponto_timeA = 0
    ponto_timeB = 0
    
    if goltimeA1 > goltimeB1:
        ponto_timeA += +3
        
    if goltimeA1 == goltimeB1:
        ponto_timeA += +1
        ponto_timeB += +1
        
    if goltimeA1 < goltimeB1:
        ponto_timeB += +3
        
    if goltimeA2 > goltimeB2:
        ponto_timeA += +3
        
    if goltimeA2 == goltimeB2:
        ponto_timeA += +1
        ponto_timeB += +1
        
    if goltimeA2 < goltimeB2:
        ponto_timeB += +3
        
        
        
    return {timeA:ponto_timeA,timeB:ponto_timeB}#Start your python function here