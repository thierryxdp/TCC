def filtraMultiplos(lista,numero):
	'''Função que retorna uma lista contendo todos os elementos da lista que recebe que são divisíveis pelo numero que também é recebido
	lista/int->lista'''
	retorno=[]
	contador=0
	quantidade_numero=len(lista)
	while (quantidade_numero>contador):
		if lista[contador]%numero==0:
			list.append(retorno,lista[contador])
		contador=contador+1
	return retorno