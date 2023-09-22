def insere(lista_numero, n):
	'''função que insere um número n em uma lista de lista_numero,
    e mantem a lista crescente, colocando n na posição certa.
    assinatura: tupla[int] > tupla[int]
    casos de teste: insere([1, 2, 3], 5) ==[1, 2, 3, 5]
    insere([16, 18, 20], 17) ==[16, 17, 18, 20]
    insere([20, 25, 30], 2) ==[2, 20, 25, 30]''' 
    list.append(lista_numero, n)
    list.sort(lista_numero)
   
    return lista_numero