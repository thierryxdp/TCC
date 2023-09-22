def maiores(lista, n):
    """ Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maior que n
    	list, int -> list
    """
    nova_lista = lista[:]
    nova_lista = [ elem for elem in lista if elem >= n]
    nova_lista.sort()
    return nova_lista