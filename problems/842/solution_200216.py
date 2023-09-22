def pontos_por_time(nome,pontos1,pontos2):
    '''funcao que retorna um dicionario cujo mapeamento sao o nome do time e o numero total de pontos da fase, sendo pontos1 cormengo e pontos2 flaminthians;str,int->str'''
    if (pontos1>pontos2):
    	return pontos1 + 3
    elif (pontos1<pontos2):
    	return pontos2 + 3
	elif (pontos1 = pontos2):
        return pontos1 + 0
    else:
        return pontos2 + 0