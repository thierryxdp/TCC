def maiores(x,n):
    """Dada uma lista1 de numeros, retorna outra lista contendo todos os numeros da lista original maiores que n e em ordem crescente
    list->list"""
    a=len(x)
    list.sort(x)
    atualizado=x[list.index(x,n):a]
    return atualizado