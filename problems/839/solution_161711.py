def carros (pessoas,capacidade = 0):
    'retorna a quantidade de carros'
    if capacidade == 0:
    	if pessoas/5 == pessoas//5:
        	return pessoas//5
    	else:
     		return pessoas//5 + 1
    else:
        if pessoas/capacidade == pessoas//capacidade:
        	return pessoas//capacidade
    	else:
     		return pessoas//capacidade + 1