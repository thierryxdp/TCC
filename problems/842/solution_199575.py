def pontos_por_time(lista):
    """
    """
    jogo1=lista[0]
    jogo2=lista[1]
    
    time1=jogo1[0]
    time2=jogo1[1]
    
    placar_jogo1=jogo1[2]
    placar_jogo2=jogo2[2]
    
    dicionario={time2:0, time1:0}
    
    #Condições Jogo1
    vitoria_time1=placar_jogo1[0]>placar_jogo1[1]
    vitoria_time2=placar_jogo1[1]>placar_jogo1[0]
    empate=placar_jogo1[0]==placar_jogo1[1]
    #Condições Jogo2
    vitoria_time1_2=placar_jogo2[0]>placar_jogo2[1]
    vitoria_time2_2=placar_jogo2[1]>placar_jogo2[0]
    empate_2=placar_jogo2[0]==placar_jogo2[1]
        
    if vitoria_time1:
        dicionario[time1] +=3
    if empate:
        dicionario[time1] +=1
        
    return dicionario