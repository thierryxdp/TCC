def maiores(lista,n):
    '''função que, dada uma lista de números inteiros e uma número n, retorna
    outra lista, que contenha todos os números da lista original maiores que n.
    list, int -> list'''
    lista1 = list()
    for i in lista:
        if i>n:
            lista1.append(i)
            return lista1
             
    return []