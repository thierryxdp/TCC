def pontos_por_time(lista):

	'''funçao que retorna o nome e a pontuaçao do time como dicionario dados a lista de entrada'''	'''list-> dic'''

	j1t1= lista[0][2][0]

	j1t2 = lista[0][2][1]

	j2t1= lista[1][2][1]

	j2t2 = lista[1][2][0]

	time1=lista[0][0]

	time2=lista[0][1]

	if j1t1 > j1t2 and j2t1 > j2t2:

		return {time1 : 6, time2 : 0}

	if j1t1 > j1t2 and j2t1 == j2t2:

		return {time1 : 4, time2 : 1}

	if j1t1 == j1t2 and j2t1 == j2t2:

		return {time1 : 2, time2 : 2}

	if j1t1 == j1t2 and j2t1 < j2t2:

		return {time1 : 1,time2 : 4}

	if j1t1 < j1t2 and j2t1 < j2t2:

		return {time1 : 0, time2 : 6}

	if j1t1 > j1t2 and j2t1 < j2t2:

		return {time1 : 3, time2 : 3}

	if j1t1 < j1t2 and j2t1 > j2t2:

		return {time1 : 3, time2 : 3}

	else: 

		if j1t1 == j1t2 and j2t1 > j2t2:

			return {time1: 4, time2 : 1}