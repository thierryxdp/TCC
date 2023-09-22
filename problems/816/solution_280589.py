def maiores(lista,n):
    """Dada uma lista de números inteiros e um número inteiro n, retorna outra
    lista que contém todos os números da lista original maiores que n; list,int->list"""
    list.append(lista,n)
    list.sort(lista)
    x=list.index(lista,n)
    return lista[x+1:]