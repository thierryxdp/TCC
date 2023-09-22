def pontos_por_time(lista):
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
    pontostime1_1=[]
    pontostime2_1=[]
    pontostime1_2=[]
    pontostime2_2=[]
   
  
    if lista[0][2][0]>lista[0][2][1]:
        pontostime1_1=pontostime1_1+[3] 
        pontostime2_1=pontostime2_1+[0]
        
    if lista[0][2][1]>lista[0][2][0]:
        pontostime2_1=pontostime2_1+[3]
        pontostime1_1=pontostime1_1+[0]
        
    if lista[0][2][1]=lista[0][2][0]:
        pontostime1_1=pontostime1_1+[1]
        pontostime2_1=pontostime2_1+[1]
        
    if lista[1][2][0]>lista[1][2][1]:
        pontostime1_2=pontostime1_2+[3]
        pontostime2_2=pontostime2_2+[0]
        
    if lista[1][2][1]>lista[1][2][0]:
        pontostime2_2=pontostime2_2+[3]
        pontostime1_2=pontostime1_2+[0]
        
    if lista[1][2][1]=lista[1][2][0]:
        pontostime1_2=pontostime1_2+[1]
        pontostime2_2=pontostime2_2+[1]
        
    total_p_time1=pontostime1_1[0]+pontostime2_2[0]
    total_p_time2=pontostime2_1[0]+pontostime1_2[1]
    dicionario={lista[0][0]:total_p_time1,lista[0][1]:total_p_time2}      
    
    return dicionario