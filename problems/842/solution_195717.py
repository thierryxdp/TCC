def pontos_por_time(jogos_da_fase):
    """retorna os numero de pontos de um time em uma fase, dados os nomes dos times e o resultado de cada um dos 2 jogos;
    list -> dict"""
    jogos_da_fase[0]=jogo1
    jogos_da_fase[1]=jogo2
    jogo1[2]=resultado1
    jogo2[2]=resultado2
    pontosA=0
    pontosB=0
    
    if resultado1[0]==resultado1[1] or resultado2[0]==resultado2[1]:
        pontosA=0
        pontosB=0
        
    if resultado1[0]<resultado1[1]:
        sum(pontosA+3)
    
    if resultado1[0]>resultado1[1]:
        sum(pontosB+3)
        
    if resultado2[0]<resultado2[1]:
        sum(pontosA+3)
        
    if resultado2[0]>resultado2[1]:
        sum(pontosB+3)
        
    return dict(jogo1[0]:pontosA,jogo2[1]:pontosB)