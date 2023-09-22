def pontos_por_time(jogos):
    """retorna a quantidade de pontos de um determinado, dado o resultado de cada um dos 2 jogos;
    list -> dict"""
    jogo1=jogos[0]
    jogo2=jogos[1]
    time1=jogo1[0]
    time2=jogo2[0]
    resultado1=jogo1[2]
    resultado2=jogo2[2]
    pontostime1=[0,0]
    pontostime2=[0,0]
    
    if resultado1:
        if resultado1[0]==resultado1[1]:
            pontostime1[0]=1
            pontostime2[0]=1
            
        elif resultado1[0]<resultado1[1]:
            pontostime2[0]=3
            
        elif resultado1[0]>resultado1[1]:
            pontostime1[0]=3
    
    if resultado2:
        if resultado2[0]==resultado2[1]:
            pontostime1[1]=1
            pontostime2[1]=1
        
        elif resultado2[0]>resultado2[1]:
            pontostime2[1]=3
        
        elif resultado2[0]<resultado2[1]:
            pontostime1[1]=3
        
    return {time1:(int(pontostime1[0])+int(pontostime1[1])),time2:(int(pontostime2[0])+int(pontostime2[1]))}#Start your python function here