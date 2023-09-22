def maiores(lista,n):
    """Dada uma lista1 de numeros, retorna outra lista contendo todos os numeros da lista original maiores que n e em ordem crescente
    list->list"""
    a=len(lista)
    list.sort(lista)
    atualizado=lista[n:a]
    return atualizado