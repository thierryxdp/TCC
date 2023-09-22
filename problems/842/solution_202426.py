def pontos_por_time(P):
    """Dividmos a lista original para obter seus termos em partes: J1 e J2 sao respectivamente Jogo 1 e Jogo 2 
    enquanto PJ1 e PJ2 sao o placar de cada jogo.
    
    """
    placar={J1[0]:0 ,J1[1]:0} """T1, time 1 e T2 : time 2"""
    
    J1=P[0]  
    J2=P[1]
    
    PJ1=J1[2]
    PJ2=J2[2]
    
    if PJ1[0] > PJ1[1]:
        placar[T1] + 3
        
    elif PJ1[0] < PJ1[1]:
    	placar[T2] + 3
        
    else:
    	placar[T1] + 1   placar[T2] + 1
    
    if PJ2[0] > PJ2[1]:
        placar[T2] + 3
        
    elif PJ1[0] < PJ1[1]:
    	placar[T1] + 3
        
    else:
    	placar[T1] + 1   placar[T2] + 1
        
    return placar