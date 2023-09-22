def pontos_por_time(jogos):
    '''
        Função que retorna o nome dos time com os pontos na fase, dada uma lista
        com as informações dos jogos de ida e volta.
        list -> dict
    '''
    placarI=jogos[0][2]
    placarV=jogos[1][2]
    time1=jogos[0][0]
    time2=jogos[0][1]
    pontosT1=0
    pontosT2=0
    if placarI[0]>placarI[1]:
        pontosT1=pontosT1+3
        
    if placarV[1]>placarV[0]:
        pontosT1=pontosT1+3
                
    if placarI[1]>placarI[0]:
        pontosT2=pontosT2+3
        
    if placarV[0]>placarV[1]:
        pontosT2=pontosT2+3
        
    if placarI[0]==placarI[1]:
    
        pontosT1=pontosT1+1
        
        pontosT2=pontosT2+1

    if placarV[0]==placarV[1]:
    
        pontosT1=pontosT1+1
        
        pontosT2=pontosT2+1
        
    return{time1:pontosT1,time2:pontosT2}