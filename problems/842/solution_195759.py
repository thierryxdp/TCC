def pontos_por_time(jogos_da_fase):
    """retorna os numero de pontos de um time em uma fase, dados os nomes dos times e o resultado de cada um dos 2 jogos;
    list -> dict"""
    jogo1=list(jogos_da_fase[0])
    jogo2=list(jogos_da_fase[1])
    resultado1=list(jogo1[2])
    resultado2=list(jogo2[2])
    pontosA=[0,0]
    pontosB=[0,0]
    
    if resultado1:
        if resultado1[0]==resultado1[1]:
            pontosA[0]=1
            pontosB[0]=1
        elif resultado1[0]<resultado1[1]:
            pontosA[0]=3
        elif resultado1[0]>resultado1[1]:
            pontosB[0]=3
    
    if resultado2:
        if resultado2[0]==resultado2[1]:
            pontosA[1]=1
            pontosB[1]=1
        
        if resultado2[0]>resultado2[1]:
            pontosA[1]=3
        
        if resultado2[0]<resultado2[1]:
            pontosB[1]=3
        
    return {jogo1[0]:(int(pontosA[0])+int(pontosA[1])),jogo1[1]:(int(pontosB[0])+int(pontosB[1]))}#Start your python function here