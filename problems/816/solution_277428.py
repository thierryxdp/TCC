def maiores(listint, n):
    """dada uma lista de numeros inteiros e um numero inteiro n, função
    retorna outra lista, contendo todos os numeros da lista original maiores que n"""
    """lista, int -> lista"""
    list.insert(listint, 2, n)
    list.sort()
    x=list.index(listint, n)
    return listint[x+1: ]