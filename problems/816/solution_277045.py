def maiores(lista, n):
    """Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista que contenha todos os 
    números da lista original maiores que n
    list, int -> list"""
    list.append(lista, n)
    list.sort(lista)
    del lista[0:list.index(lista, n)+1]
    list.count(lista, n)
    del lista[0:list.index(lista, n)+list.count(lista, n)]
    return lista