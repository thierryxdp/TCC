def pontos_por_time(x):
    '''A função verifica os pontos de cada time
    vitória = 3 pontos
    empate = 1 ponto
    lista, lista -> dicionário'''
    
    timea = x[0][0]
    timeb = x[0][1]
    
    time1 = []
    time2 = []
    time1a = []
    time2a = []
    
    
    if x[0][2][0] > x[0][2][1]:
        list.append(time1,3,)
    elif x[0][2][0] == x[0][2][1]:
        list.append(time1,1,)
        list.append(time2,1,)
    elif x[0][2][0] < x[0][2][1]:
        list.append(time2,3,)
    if x[1][2][0] > x[1][2][1]:
        list.append(time1,3,)
    elif x[1][2][0] == x[1][2][1]:
        list.append(time1,1,)
        list.append(time2,1,)
    elif x[1][2][0] < x[1][2][1]:
        list.append(time2,3,)
        
    return time2