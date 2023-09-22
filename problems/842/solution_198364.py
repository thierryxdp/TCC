def pontos_por_time(x):
    '''	
    	recebe uma lista que possui outras duas listas como seus elementos e que possui o numero de 
        gols em dois jogos de futebol entre dois times e retorna um dicionario com o nome do time
        e o seu total de pontos na fase
    '''
    pontoTime1 = 0
    pontoTime2 = 0
    a = x[0][2][0] - x[0][2][1]
    if a < 0:
        pontoTime2 = pontoTime2+3
    if a > 0:
        pontoTime1 = pontoTime1+3
    else:
        pontoTime1 = pontoTime1+1
        pontoTime2 = pontoTime2+1
    a = x[1][2][0] - x[1][2][1]
    if a < 0:
        pontoTime1 = pontoTime1+3
    if a > 0:
        pontoTime2 = pontoTime2+3
    else:
        pontoTime1 = pontoTime1+1
        pontoTime2 = pontoTime2+1
    return {x[0][0]:pontoTime1, x[0][1]:pontoTime2}