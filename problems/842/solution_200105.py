def pontos_por_time(lista):
    '''
    funcao que recebe uma lista de 2 
    elementos que sao tambem uma lista
    '''
    t1 = 0
    t2 = 0
    jogo1 = lista[0]
    pontos_jogo1 = jogo1[2]
    if pontos_jogo1[0] > pontos_jogo1[1]:
    	t1 = 3
    	t2 = 0
    if pontos_jogo1[0] == pontos_jogo1[1]:
    	t1 = 1
    	t2 = 1
    if pontos_jogo1[0] < pontos_jogo1[1]:
    	t1 = 0
    	t2 = 3

	t3 = 0
    t4 = 0

    jogo2 = lista[1]
    pontuacao_jogo2 = jogo2[2]
    
    if pontuacao_jogo2[0] > pontuacao_jogo2[1]:
    	t3 = 3
    	t4 = 0

    if pontuacao_jogo2[0] == pontuacao_jogo2[1]:
    	t3 = 1
    	t4 = 1

    if pontuacao_jogo2[0] < pontuacao_jogo2[1]:
    	t3 = 0
    	t4 = 3

    pontuacaot1 = t1 + t4
    pontuacaot2 = t2 + t3

    return {jogo1[0]:pontuacaot1,jogo1[1]:pontuacaot2}