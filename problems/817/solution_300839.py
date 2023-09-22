def maiores(lista,n):
	""" Esta função insere e ordena todos os numeros maiores que n em ordem crescente
	list, int -> list """
	#adiciona o numero solto a lista
	list.append(lista,n)
	#ordena a lista
	list.sort(lista)
	#ordena os maiores 
	lista_final = lista[list.index(lista,n)+1:]

	return lista_final
	
	def acima_da_media(lista):

	soma = sum(lista)
	
	x = len(lista)
	
	media = soma/x

	return maiores(lista, media)