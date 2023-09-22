def quem_ganhou(gols_a, gols_b, partida):
    if gols_a[partida] == gols_b[partida]:
		return (1, 1)
    
    return (3, 0) if gols_a[partida] > gols_b[partida] else (0, 3)

def pontos_por_time(jogos):
    ''' Retorna um dicionário com a sendo a chave o nome do time e o valor a pontuação
    list -> dict '''
    
    time_a, time_b = jogos[0][0], jogos[0][1]
    pts_a, pts_b = 0, 0
    
    gols_a = (jogos[0][2][0], jogos[1][2][1])
    gols_b = (jogos[0][2][1], jogos[1][2][0])
    
    pts = quem_ganhou(gols_a, gols_b, partida = 0)
    pts_a += pts[0]
    pts_b += pts[1]
    
    pts = quem_ganhou(gols_a, gols_b, partida = 1)
    pts_a += pts[0]
    pts_b += pts[1]
	
    resultado = {time_a: pts_a, time_b: pts_b}
    
    return resultado