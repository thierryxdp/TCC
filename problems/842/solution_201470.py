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
    
    pontuacao = {}
    if ( resultado(lista_gols[0][2]) == 0): # empate primeiro jogo
        pontuacao[lista_fase[0][0]] = 1
        pontuacao[lista_fase[0][1]] = 1
    elif ( resultado(lista_fase[0][2]) == 1): # vitoria time casa
        pontuacao[lista_fase[0][0]] = 3
        pontuacao[lista_fase[0][1]] = 0
    else: # vitoria time visitante
        pontuacao[lista_fase[0][0]] = 0
        pontuacao[lista_fase[0][1]] = 3
    
    return pontuacao