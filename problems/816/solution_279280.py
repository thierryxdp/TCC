def maiores(lista,n):
    '''função que, dada uma lista de números inteiros e uma número n, retorna
    outra lista, que contenha todos os números da lista original maiores que n.
    list, int -> list'''
    lista_oredenada = lista.sort()
    for m in lista:
        if m > n:
            lista_nova = del.lista[m:]
            return lista_nova
     return []