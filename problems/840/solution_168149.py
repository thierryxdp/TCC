def bolos(farinha,ovo,leite):
    '''funcao que calcula a quantidade de bolos
    que podem ser feitos a partir de uma receita e
    uma dada quantidade de ingredientes'''
    if (farinha/2)<((ovo/3)==(leite/5)):
    	return int(farinha/2)
    elif (ovo/3)<((farinha/2)==(leite/5)):
    	return int(ovo/3)
    elif (leite/5)<((ovo/3)==(farinha/2)):
        return int(leite/5)
    else:
	    return int(((farinha/2)+(ovo/3)+(leite/5))/3)