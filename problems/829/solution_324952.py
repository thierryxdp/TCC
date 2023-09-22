def soma_h(numero):
    '''funcao que calcula e retorna o valor h com n termos'''
    cont = 0.0
    for i in range(1, numero+1):
        cont += 1/i
	return round(cont,2)