def maiores(lista, n):
    """Função que recebe uma lista de números inteiros e um
    número inteiro n. A função retorna outra lista que contenha
    todos os números da lista original maiores que número n, 
    ordenados em ordem crescente.
    list,int->list
    """
    nova_lista = lista + [n]
    list.sort(nova_lista)
    a = list.index(nova_lista, n), b = list.count(nova_lista, n)
    return nova_lista[ a + b : ]