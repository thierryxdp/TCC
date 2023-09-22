def pontos_por_time(jogos):
    '''xxxxxxxx'''
    '''xxxxxxxx'''
    time1 = jogos [0][0]
    time2 = jogos [0][1]
    
    time1_ida = jogos [0][2][0]
    time2_ida = jogos [0][2][1]
    
    time1_volta = jogos [1][2][0]
    time2_volta = jogos [1][2][1]
    
    pontos_time1 = 0
    pontos_time2 = 0
    
    auxponto1 = 0
    auxponto2 = 0
    
    if time1_ida > time2_ida:
        pontos_time1 = 3
        elif time2_ida > time1_ida:
            pontos_time2 = 3
            else:
                pontos_time1 = 1
                pontos_time2 = 1
     
    if time1_volta > time2_volta:
        auxponto1 = 3
        elif time2_volta > time1_volta:
            auxponto2 = 3
            else:
                auxponto1 = 1
                auxponto2 = 1
    if time1 == jogos [1][0]:
        pontos_time1 += auxponto1
        pontos_time2 += auxponto2
        else:
            pontos_time1 += auxponto2
            pontos_time2 += auxponto1
            
    if pontos_time1 >= pontos_time2:
        return {time1:pontos_time1, time2:pontos_time2}
        else:
            return {time2:pontos_time2, time1:pontos_time1}