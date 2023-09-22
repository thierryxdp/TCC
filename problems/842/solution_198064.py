def pontos_por_time(jogos):
    '''
    Função que recebe uma lista de dois elementos, onde
    cada elemento é também uma lista. A lista completa 
    traz informações sobre num de gols em jogos de futebol entre 2 times,
    no formato [['Cormengo','Flamínthians',[1,0]],[Flamínthians','Cormengo',[2,2]]]. 
    No exemplo o resultado do primeiro jogo seria 1x0 a favor do Cormengo. A função 
    retorna um dicionário cujos mapeamentos são <nome do time> -. <numero total de pontos na fase>
    Os times recebem um ponto por empate e três por vitória. O valor de pontos na derrota é 0.
    O total de pontos da fase é a soma dos pontos dos dois jogos da fase.
    list->dict
    '''
    pontos1=0
    pontos2=0
    jogo_1=jogos[0]
    jogo_2=jogos[1]
    time1=jogo_1[0]
    time2=jogo_1[1]
   
   
    gol1_1=jogo_1[2][0]
    gol1_2=jogo_1[2][1]
    
    if gol1_1>gol1_2:
        pontos1+=3
        
    elif gol1_2>gol1_1:
        pontos2+=3
            
    elif gol1_2==gol1_1:
        pontos1+=1
        pontos2+=1
        
    
   
    gol2_1=jogo_2[2][1]
    gol2_2=jogo_2[2][0]
    
    if gol2_1>gol2_2:
        pontos1+=3
        
    elif gol2_2>gol2_1:
        pontos2+=3
            
    elif gol2_2==gol2_1:
        pontos1+=1
        pontos2+=1
        
    
    return {time1:pontos1,time2:pontos2}