def pontos_por_time(P):
    """Dividmos a lista original para obter seus termos em partes: J1 e J2 sao respectivamente Jogo 1 e Jogo 2 
    enquanto PJ1 e PJ2 sao o placar de cada jogo.
    
    """
    
    J1=P[0]  """ [[T1 ,T2, [PJ1,PJ1]],[T2, T1 ,[PJ2,PJ2]]]"""
    J2=P[1]
    
    PJ1=J1[2]
    PJ2=J2[2]
    
    PJ1T1=PJ1[0]
    PJ1T2=PJ1[1]
    
    PJ2T2=PJ2[0]
    PJ2T1=PJ2[1]
    
    if PJ1T1[] > PJ1T2[]:  """PJ1[0] Cormengo , PJ1[1] Flaminthinas"""
     	placar[T1] =+ 3
        
    elif PJ1T1[] < PJ1T2[]:
    	placar[T2] =+ 3
        
    else:
    	placar[T1] =+ 1 
        placar[T2] =+ 1
    
    if PJ2T2[] > PJ2T1[]:
        placar[T2] =+ 3
        
    elif PJ1T2[] < PJ1T1[]:
    	placar[T1] =+ 3
        
    else:
    	placar[T1] =+ 1 
        placar[T2] =+ 1
        
    return placar