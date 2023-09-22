def repetidos(ls):
    '''Função que recebe uma lista de números como entrada, e retorna o número de vezes 
que um elemento da lista é igual ao elemento anterior.
Assinatura: ls -> int
Casos de teste:
repetidos([24, 14, 9, 29, 5, 13, 27, 22, 8, 18, 18, 15, 12, 12]) == 2
repetidos([20, 20, 1, 29, 26, 26, 7, 7]) == 3
repetidos([4, 26, 11, 11, 23, 19, 28, 5, 20, 10]) == 1
'''
	new_ls = []
    repetidos = []
	for n in ls:
		if n in new_ls:
			repetidos.append(n)
		else:
			new_ls.append(n)
	return len(set(repetidos))