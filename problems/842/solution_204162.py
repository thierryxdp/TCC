def pontos_por_time(lista):
    '''
    funcao que recebe uma lista de dois elementos, onde cada
    elemento e uma lista, a lista completa tem informações do
    número de gols em dois jogos de futebol entre dois times 
    (jogo da ida - jogo1  e jogo da volta -jogo2), e retorna
    um dicionario cujos mapeamentos são: <nome do time> -> 
    <numero total de pontos na fase>
    :param lista: list
    :return: dict
    '''
    time_A = 0
    time_B = 0

    jogo1 = lista[0]
    pontuacaoJogo1 = jogo1[2]
    
    if pontuacaoJogo1[0] > pontuacaoJogo1[1]:
    	time_A = 3
    	time_B = 0

    if pontuacaoJogo1[0] == pontuacaoJogo1[1]:
    	time_A = 1
    	time_B = 1

    if pontuacaoJogo1[0] < pontuacaoJogo1[1]:
    	time_A = 0
    	time_B = 3


    time_C = 0
    time_D = 0

    jogo2 = lista[1]
    pontuacaoJogo2 = jogo2[2]
    
    if pontuacaoJogo2[0] > pontuacaoJogo2[1]:
    	time_C = 3
    	time_D = 0

    if pontuacaoJogo2[0] == pontuacaoJogo2[1]:
    	time_C = 1
    	time_D = 1

    if pontuacaoJogo2[0] < pontuacaoJogo2[1]:
    	time_C = 0
    	time_D = 3

    pontuacaotimeA = time_A + time_D
    pontuacaotimeB = time_B + time_C

    return {jogo1[0]:pontuacaotimeA,jogo1[1]:pontuacaotimeB}