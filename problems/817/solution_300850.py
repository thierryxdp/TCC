def maiores(lista,n):
	""" Esta função insere e ordena todos os numeros maiores que n em ordem crescente
	list, int -> list """
	#adiciona o numero solto a lista
	list.append(lista,n)
	#ordena a lista
	list.sort(lista)
	#ordena os maiores 
	lista_final = lista[list.index(lista,n) + list.count(lista,n):]

	return lista_final
	
def acima_da_media(lista):
	""" Esta função calcula a media de uma lista
	list,int ->list
	list -> list """
	soma = sum(lista) 
	
	x = len(lista)
	
	media = soma/x

	return maiores(lista, media)