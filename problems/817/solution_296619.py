def insere(lista_numero,n):
	"""insere um numero dentro de uma ordem crescente.
entra lista de numeros e o numero que deseja acrescentar(n);
list[int],int->list[int]
obs: a quantidade de elementos varia conforme a lista de numeros"""
	list.append(lista_numero,n)
	list.sort(lista_numero)
	return lista_numero
def maiores(lista_numero,n):
	"""entra lista de numeros e retorna lista com numeros maiores que um numero desejado(n);
list[int],int->list[int]."""
	insere(lista_numero,n)
	return lista_numero[list.index(lista_numero,n)+1:]
def acima_da_media(lista_numero):
	"""entra lista com notas(lista_numero) e retorna lista com apenas valores acima da media(n).
list[float],int->list[float]"""
	n=(sum(lista_numero[:]))/len(lista_numero)
	return maiores(lista_numeros,n)