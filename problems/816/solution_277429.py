def maiores(listint, n):
    """dada uma lista de numeros inteiros e um numero inteiro n, função
    retorna outra lista, contendo todos os numeros da lista original maiores que n"""
    """lista, int -> lista"""
    lista = listint
    list.insert(lista, 2, n)
    lista.sort()
    list2=list.index(lista, n)
    return lista[list2+1: ]