def pontos_por_time(lista):
    """função que recebe uma lista com dois elementos onde contem as informações de duas partidas de futebol entre dois times e retorna um dicionario
	informando o total de pontos de cada time
	list -> dict"""
    
    pontosjogo1_time1 = 0
    pontosjogo2_time1 = 0
    pontosjogo1_time2 = 0
    pontosjogo2_time2 = 0
    
    nome1 = lista[0][0]
    nome2 = lista[0][1]
    
    jogo1 = lista[0][2]
    jogo2 = lista[1][2]
    
    if jogo1[0] > jogo1[1]:
        pontosjogo1_time1 = 3
    elif jogo1[0] < jogo1[1]:
        pontosjogo1_time2 = 3
    else:
        pontosjogo1_time1 = 1
        pontosjogo1_time2 = 1
    
    if jogo2[1] > jogo2[0]:
        pontosjogo2_time1 = 3
    elif jogo2[1] < jogo2[0]:
        pontosjogo2_time2 = 3
    else:
        pontosjogo2_time1 = 1
        pontosjogo2_time2 = 1
        
    resultado_time1 = pontosjogo1_time1 + pontosjogo2_time1
    resultado_time2 = pontosjogo1_time2 + pontosjogo2_time2
    
    return {nome1: resultado_time1, nome2: resultado_time2}