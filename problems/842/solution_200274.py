def pontos_por_time(nome1,nome2,pontos1,pontos2):
    '''funcao que retorna um dicionario cujo mapeamento sao o nome do time e o numero total de pontos da fase, sendo pontos1 cormengo e pontos2 flaminthians;str,int->str'''
    dicio = {nome1: " ",
             nome2: " "}
    if(pontos1>pontos2):
    	return [nome1 + [pontos1 + 3] + [nome2 + pontos2]
    elif(pontos2>pontos1):
    	return dicio[nome2 + [pontos2 + 3] + [nome1 + pontos1]
	elif(pontos1==pontos2):
        return dicio[nome1 + pontos1] + [nome2 + pontos2]
    elif(pontos2==pontos1):
     	return dicio[nome2 + pontos2] + [nome1 + pontos1]
    else: 
        return dicio[nome1 + pontos1] + [nome2 + ponto2]