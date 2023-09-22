def resultado(lista_gols):
    """ Recebe uma lista de gols de ambos os times participantes e visitantes e retorna 
    1 se o time da casa venceu, -1 se o visitante venceu e 0 caso tenha ocorrido empate.
    
    list-> int """
    
    if(lista_gols[0] > lista_gols[1]):
        return 1
    elif(lista_gols[0] < lista_gols[1]):
        return -1
    else: 
        return 0

def pontos_por_time(lista_fase):
    """ Recebe uma lista que contem o placar de dois jogos e retorna a pontuação final dos times 
    participantes.
    
    list -> dict """
    
    pontuacao = {lista_fase[0][0]: 0, lista_fase[0][1]: 0}
    
    # Forma alternativa
    # pontuacao = {}
    # pontuacao[lista_fase[0][0]] = 0
    # pontuacao[lista_fase[0][1]] = 0
    
    # Alterando as pontuações de acordo com o jogo
    i = 0
    while (i<2):
        if ( resultado(lista_fase[i][2]) == 0): # empate primeiro jogo
        	pontuacao[lista_fase[i][0]] += 1
        	pontuacao[lista_fase[i][1]] += 1
    	elif ( resultado(lista_fase[i][2]) == 1): # vitoria time casa
        	pontuacao[lista_fase[i][0]] += 3
        
    	else: # vitoria time visitante
        	pontuacao[lista_fase[i][1]] += 3
        
        i += 1
        
    
    return pontuacao