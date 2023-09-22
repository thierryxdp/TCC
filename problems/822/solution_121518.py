def repetidos(num):
	'''
    Dada uma lista de numeros, retorna-se o numero de vezes
    que o numero de index x e igual ao de x 
    '''
    i, cont = 1, 0
    while i < len(num):
        if num[i] == num[i - 1]:
            cont += 1
		i += 1
	return cont