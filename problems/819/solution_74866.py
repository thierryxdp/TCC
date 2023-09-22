def filtraMultiplos(lista,numero):
	'''Função que filtra os números múltiplos de uma lista, considerando um número dado.
	Entrada: list,int
	Saída: list'''

	multiplos=[]
	proximo=0

	while proximo < len(lista):
		if lista[proximo]%numero==0:
			multiplos=multiplos+[lista[proximo],]
		proximo=proximo+1

	return multiplos