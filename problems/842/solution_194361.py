def pontos_por_time(lista):
    """retorna o vencedor entre os times
	lista->dict"""
    
    d = {
        lista[0][0]: 0, 
        lista[0][1]: 0
    }

    partida = lista[0]

    if partida[2][0] < partida[2][1]:
        d[partida[1]] += 3
    elif partida[2][0] > partida[2][1]:
        d[partida[0]] += 3
    else:
        d[partida[0]] += 1
        d[partida[1]] += 1
    
    partida = lista[1]
   	
    if partida[2][0] < partida[2][1]:
        d[partida[1]] += 3
    elif partida[2][0] > partida[2][1]:
        d[partida[0]] += 3
    else:
        d[partida[0]] += 1
        d[partida[1]] += 1
        
    return d