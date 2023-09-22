def pontos_por_time(lista):
    ''' documentação
    list->dict'''
    
    timeA = lista[0][0]
    timeB = lista[0][1]
    
    goltimeA1 = lista[0][2][0]
    goltimeB1 = lista[0][2][1]
    
    timeA == lista[1][1]
    timeB == lista[1][0]
    
    goltimeA2 = lista[0][2][1]
    goltimeB2 = lista[1][2][0]
    
    ponto_timeB = goltimeB1 + goltimeB2
    ponto_timeA = goltimeA1 + goltimeA2
    
    return {timeA:ponto_timeA,timeB:ponto_timeB}

    timeA = lista[0][0]
    timeB = lista[0][1]
    
    goltimeA1 = lista[0][2][0]
    goltimeB1 = lista[0][2][1]
    
    timeA == lista[1][1]
    timeB == lista[1][0]
    
    goltimeA2 = lista[1][2][0]
    goltimeB2 = lista[1][2][1]
    
    pontos_timeA = 0
    pontos_timeB = 0
    
    goltimeB = goltimeB1 + goltimeB2
    
    ponto_timeA = goltimeA1 + goltimeA2
    ponto_timeB = goltimeB1 + goltimeB2
    
    return {timeA:ponto_timeA,timeB:ponto_timeB}#Start your python function here