def maiores(lista,n):
    """Dada uma lista1 de numeros, retorna outra lista contendo todos os numeros da lista original maiores que n e em ordem crescente
    list->list"""
    list.reverse(lista)
    x=len(lista)
    a=list.index(lista,n)
    return lista