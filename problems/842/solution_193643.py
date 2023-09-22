def pontos_por_time(gols):
    """A função atribui para cada valor de gol de cada partida uma variável,
    compara os gols para receber a informação de quem foi o vencedor e adiciona
    pontos de acordo com o resultado para cada time, após conferir os dois jogos
    preeche um dicionário com o nome dos times e quantos pontos cada um possuiu
    após os jogos.
    lista-> dicionário"""
    ponto_a=0
    ponto_b=0
    gol_a_1=gols[0][2][0]
    gol_b_1=gols[0][2][1]
    gol_b_2=gols[1][2][0]
    gol_a_2=gols[1][2][1]
    time_a=gols[0][0]
    time_b=gols[0][1]
    resultado={}
    
    if gol_a_1>gol_b_1:
    	ponto_a+=3
    elif gol_a_1==gol_b_1:
    	ponto_a+=1
        ponto_b+=1
    else:
        ponto_b+=3
        
	if gol_a_2>gol_b_2:
    	ponto_a+=3
    elif gol_a_2==gol_b_2:
    	ponto_a+=1
        ponto_b+=1
    else:
        ponto_b+=3
    
    resultado[time_a]=ponto_a
    resultado[time_b]=ponto_b
    return resultado