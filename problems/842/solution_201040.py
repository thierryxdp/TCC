def pontos_por_time(jogo):
    '''
    '''
    pontos= {}
    
    
    time1= jogo[0][2][0]
    time2= jogo[0][2][1]
    
    if jogo [0][2][0] > jogo[0][2][1]:
        pontos[time1]=3
    elif jogo [0][2][1] > jogo[0][2][0]:
        pontos[time2]=3
    else:
        pontos[time1]=2
        pontos[time2]=2
        
    time1= jogo[1][2][1]
    time2= jogo[1][2][0]
    
    if  jogo [1][2][1] > jogo[1][2][0]:
        pontos[time1]+=3
    elif jogo [1][2][0] > jogo[1][2][1]:
        pontos[time2]+=3
    else:
        pontos[time1]+=2
        pontos[time2]+=2
        
    return pontos