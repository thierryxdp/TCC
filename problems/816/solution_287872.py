def maiores(l,n):
    """função que dada uma lista de numeros inteiros e uma numero inteiro n,retorna outra lista que tenha todos os numeros da lista original maiores que n list->list"""
    list.append(l,n)
    list.sort(l)
    f=list.index(l,n)
    return l[f+1:]