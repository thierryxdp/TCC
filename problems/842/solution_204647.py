def pontos_por_time(x):
    """A função calcula a quantidade de pontos feitos por cada time em dois jogos e retorna em um dicionario o resultado
    list --> disc"""
    r = {}
    time1 = 0
    time2 = 0
    if x[0][2][0] < x[0][2][1]:
        time2 = time2 + 3
	elif x[0][2][0] > x[0][2][1]:
        time1 = time1 + 3
	elif x[0][2][0] == x[0][2][1]:
        time1 = time1 + 1
        time2 = time2 + 1
        
    if x[1][2][0] > x[1][2][1]:
        time2 = time2 + 3
	elif x[1][2][0] < x[1][2][1]:
        time1 = time1 + 3
	elif x[1][2][0] == x[1][2][1]:
        time1 = time1 + 1
        time2 = time2 + 1
    r[x[0][0]] = time1
    r[x[0][1]] = time2
    return r