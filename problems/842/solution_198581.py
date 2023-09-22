def pontos_por_time(x):
    ''''''
    
    
    jogo_ida_time1 = [x[0][0],x[0][2][0]]
    jogo_ida_time2 = [x[0][1],x[0][2][1]]
        
    jogo_volta_time1 = [x[1][0],x[1][2][0]]
    jogo_volta_time2 = [x[1][1],x[1][2][1]]
    
    
    
    pontos = dict()
    
    if jogo_ida_time1[1] > jogo_ida_time2[1]:
        
        jogo_ida_time1 +[3]
        
    elif jogo_ida_time1[1] < jogo_ida_time2[1]:
        
        jogo_ida_time2 +[3] 
    
    else:
        
        jogo_ida_time1 +[1]
        jogo_ida_time2 +[1]
    
    
    
    
    if jogo_volta_time1[1] > jogo_volta_time2[1]:
        
        jogo_volta_time1 +[3]
        
    elif jogo_volta_time1[1] < jogo_volta_time2[1]:
        
        jogo_volta_time2 +[3] 
    
    else:
        
        jogo_volta_time1 +[1]
        jogo_volta_time2 +[1]
    
    
    
    
    if jogo_volta_time1[0] == jogo_ida_time1[0]:
        
        pontos = {jogo_volta_time1[0]: [jogo_volta_time1[2] + jogo_ida_time1[2]]\
    			  jogo_volta_time2[0]: [jogo_volta_time2[2] + jogo_ida_time2[2]]}