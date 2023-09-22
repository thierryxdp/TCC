def pontos_por_time(lista):
    '''função que recebe uma lista de dois elementos, 
    em forma de lista e retorna seu dicionário com o total de 
    pontos do time na fase list,list--->dic'''
    
    timea = 0
    timeb = 0

    jogo1 = lista[0]
    pontuacaoJogo1 = jogo1[2]
    
    if pontuacaoJogo1[0] > pontuacaoJogo1[1]:
    	timea = 3
    	timeb = 0

    if pontuacaoJogo1[0] == pontuacaoJogo1[1]:
    	timea = 1
    	timeb = 1

    if pontuacaoJogo1[0] < pontuacaoJogo1[1]:
    	timea = 0
    	timeb = 3


    timec = 0
    timed = 0

    jogo2 = lista[1]
    pontuacaoJogo2 = jogo2[2]
    
    if pontuacaoJogo2[0] > pontuacaoJogo2[1]:
    	timec = 3
    	timed = 0

    if pontuacaoJogo2[0] == pontuacaoJogo2[1]:
    	timec = 1
    	timed = 1

    if pontuacaoJogo2[0] < pontuacaoJogo2[1]:
    	timec = 0
    	timed = 3

    pontuacaotimea = timea + timed
    pontuacaotimeb = timeb + timec

    return {jogo1[0]:pontuacaotimea,jogo1[1]:pontuacaotimeb}#Start your python function here