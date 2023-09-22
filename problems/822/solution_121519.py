def repetidos(num):
	'''
    Dada uma lista de numeros, retorna-se a quantidade de vezes
    que o numero de index x e igual ao de x - 1. 
    
    Entrada/Saida:
    list -> int
    '''
    i, cont = 1, 0
    while i < len(num):
        if num[i] == num[i - 1]:
            cont += 1
		i += 1
	return cont