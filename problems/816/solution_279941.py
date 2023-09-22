def maiores (lista, n):
	''' funcao que dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n;
lista , int -> lista '''
	list.append(lista, n)
    list.sort(lista)
    indice = list.index(lista, n)
    return lista[indice+1:]