def maiores(lista,n):
    '''função que, dada uma lista de números inteiros e uma número n, retorna
    outra lista, que contenha todos os números da lista original maiores que n.
    list, int -> list'''
    lista_oredenada = lista.sort()
    if n in lista:
        i = lista.index(n)
        listanova1 = (lista[i:])
        return listanova1
    return []