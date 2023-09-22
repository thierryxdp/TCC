def pontos_por_time(jogos):
    ''' Retorna um dicionário com a sendo a chave o nome do time e o valor a pontuação
    list -> dict '''
    
    time_a, time_b = jogos[0][0], jogos[0][1]
    pts_a, pts_b = 0, 0
    
    gols_a = (jogos[0][2][0], jogos[1][2][1])
    gols_b = (jogos[0][2][1], jogos[1][2][0])
    
    if gols_a[0] == gols_b[0]:
        pts_a += 1
        pts_b += 1
	elif gols_a[0] > gols_b[0]:
        pts_a += 3
    else:
        pts_b += 3
	
    if gols_a[1] == gols_b[1]:
        pts_a += 1
        pts_b += 1
    elif gols_a[1] > gols_b[1]:
        pts_a += 3
    else:
        pts_b += 3
	
    resultado = {time_a: pts_a, time_b: pts_b}
    
    return resultado