def pontos_por_time(P):
    """Dividmos a lista original para obter seus termos em partes: J1 e J2 sao respectivamente Jogo 1 e Jogo 2 
    enquanto PJ1 e PJ2 sao o placar de cada jogo.
    
    [[T1 ,T2, [PJ1,PJ1]],[T2, T1 ,[PJ2,PJ2]]]
    
    """
    
    J1=P[0] 
    J2=P[1]
    
    PJ1=J1[2]
    PJ2=J2[2]
    
    
    if PJ1[0] > PJ1[1]:  
    	P1T1=3
    	P1T2=0
        
    elif PJ1[0] < PJ1[1]:
        P1T1=0
        P1T2=3
    	
        
    else:
    	P1T1=1
        P1T2=1
        
    if PJ2[0] < PJ2[1]:
        P2T1=0
        P2T2=3
        
    elif PJ1[0] > PJ1[1]:
    	P2T1=3
        P2T2=0
        
    else: 
    	P2T1=1
        P2T2=1
        
        PT1=P1T1+P2T1
        PT2=P1T2=P1T2
        
        resultado={J1[0]:PT1,J1[1]:PT2}
    
    return resultado