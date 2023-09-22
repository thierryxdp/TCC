def pontos_por_time(jogos):
    """recebe duas listas, cada uma referente a uma partida de futebol,
    e cada uma sendo composta por duas listas, a primeira contendo os dois 
    times daquela partida, e a segunda, seus respectivos gols e retorna um
    dicionario que atribui os pontos de cada time aos seus nomes
    vitoria = 3 pontos, empate = 1 ponto e derrota = 0 pontos
    lista, lista -> dicionario"""
    
    jogo1 = jogos[0]
    jogo2 = jogos[1]
    
    time1 = jogo1[0][0]
    time2 = jogo1[0][1]
    
    pontos1 = 0
    pontos2 = 0
    
    #jogo1
    gols11 = jogo1[1][0]
    gols12 = jogo1[1][1]
    
    if (gols11 > gols12):
        pontos1 += 3
        
    elif (gols12 > gols11):
        pontos2 += 3
        
    elif (gols11 == gols12):
        pontos1 += 1
        pontos2 += 2
        
    #jogo2
    gols21 = jogo2[1][1]
    gols22 = jogo2[1][0]
        
        
    if (gols21 > gols22):
        pontos1 += 3
        
    elif (gols22 > gols21):
        pontos2 += 3
        
    elif (gols21 == gols22):
        pontos1 += 1
        pontos2 += 1
        
    return {time1:pontos1, time2:pontos2}