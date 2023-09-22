def pontos_por_time(lista):

	jogo1=int[lista[0][2][0],lista[0][2][1]]	
    jogo2=int[lista[1][2][1],lista[1][2][0]]

	time1=lista[0][0]

	time2=lista[0][1]

	if jogo1[0]>[1] and jogo2[0]>[1]:

		return {time1 : 6, time2 : 0}

	if jogo1[0]>[1] and jogo2[0]==[1]:

		return {time1 : 4, time2 : 1}

	if  jogo1[0]==[1] and jogo2[0]==[1]:

		return {time1 : 2, time2 : 2}

	if jogo1[0]==[1] and jogo2[0]<[1]:

		return {time1 : 1, time2 : 4}

	if jogo1[0]<[1] and jogo2[0]<[1]:

		return {time1 : 0, time2 : 6}

	if jogo1[0]>[1] and jogo2[0]<[1]:

		return {time1 : 3, time2 : 3}

	else:

		if jogo1[0]<[1] and jogo2[0]>[1]:

			return {time1 : 3, time2 : 3}