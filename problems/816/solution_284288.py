def maiores(lista,n):
    """Função que, dada uma lista de números inteiros e um número n, retorna outra lista, que contém todos os números da lista original maiores que n, ordenados em ordem crescente; lista,int->lista"""
    list.append(lista,n)
    list.sort(lista)
    lista_final = list.index(lista,n)
    return lista[lista_final+1:]