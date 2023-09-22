def maiores(lista, n):
    """funcao que dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista
    contendo todos os numeros da lista original maiores que n, ordenados em ordem crescente;
    list, int -> list"""
    list.insert(lista, 1, n)
    list.sort(lista)
	if max(lista) == n:
        return []