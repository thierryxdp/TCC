def insere(lista_numero, n):
	''' funcao que dada uma lista ordenada (crescente) de numeros inteiros e um numero inteiro n inclua n na posicao correta;
lista , int , float , complex -> lista '''
    lista_numero1 = lista_numero[:]
	list.append(lista_numero1,n)
	list.sort(lista_numero1)
	return (lista_numero1) - (insere(lista_numero, n))