def pontos_por_time(lista):
    """A função receberá como entrada uma lista de dois elementos em que
    cada elemento também é uma lista. A mesma retornará um dicionário com
    mapeamento pelo nome do time informando o número total de pontos na
    fase.
    list -> dict"""
    
    lista1=lista[0]
    lista2=lista[1]
    
    time1=lista1[0]
    time2=lista1[1]
    placar1=lista1[2]
    
    time3=lista2[0]
    time4=lista2[1]
    placar2=lista2[2]
    
    ponto1=placar1[0]
    ponto2=placar1[1]
    ponto3=placar2[0]
    ponto4=placar2[1]
    
    if ponto1>ponto2:
        saldotime1=3
    
    if ponto1==ponto2:
        saldotime1=1
        saldotime2=1
        
    if ponto1<ponto2:
        saldotime2=3
        
    if ponto3>ponto4:
        saldotime3=3
        
    if ponto3==ponto4:
        saldotime3=1
        saldotime4=1
        
    if ponto3<ponto4:
        saldotime4=3
        
    if time1==time3:
    	resultado1 = saldotime1+saldotime3
        resultado2 = saldotime2+saldotime4
        
    else:
        resultado1 = 0
        resultado2 = 0
        
    if time2==time3:
        	resultado3 = saldotime2+saldotime3
            resultado4 = saldotime1+saldotime4
            
    else:
        resultado3 = 0
        resultado4 = 0
        
    jogo = {"time1":"resultado1+resultado3", "time2":"resultado2+resultado4"    
        
	return: jogo