def pontos_por_time(nome1,nome2,pontos1,pontos2):
    '''funcao que retorna um dicionario cujo mapeamento sao o nome do time e o numero total de pontos da fase, sendo pontos1 cormengo e pontos2 flaminthians;str,int->str'''
    dicio = {nome1: ' ',
             nome2: ' '}
    if (pontos1>pontos2):
    	return [nome1 + [pontos1 + 3] + nome2 +[pontos2 + 0]]
    elif (pontos1<pontos2):
    	return [nome2 + [pontos2 + 3] + nome1 + [pontos1+0]]
	elif (pontos1==pontos2):
        return [[nome1 + [pontos1 + 0] + nome2 + [pontos2 + 0]]
    else:
        return [nome2 + [pontos2 + 0] + nome1 + [pontos1 + 0]]