def maiores(lista,n):
    """Dada uma lista de números inteiros e um n´´umero inteiro n, retorna todos os números da lista original maiores do que n.
    list,int->int"""
    lista.append(n)
    list.sort(lista)
    x=list.index(lista,n)
    return lista[x+1:]