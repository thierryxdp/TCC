def maiores(lista,n):
    '''função que, dada uma lista de números inteiros e uma número n, retorna
    outra lista, que contenha todos os números da lista original maiores que n.
    list, int -> list'''
    
    lista_com_n = lista.insert([0],n)
    lista_ordenada = lista.sort()
    i = lista.index(n)
    del lista_ordenada[i:]
    return lista_ordenada