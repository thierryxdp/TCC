def maiores(lista,n):
    '''função que, dada uma lista de números inteiros e uma número n, retorna
    outra lista, que contenha todos os números da lista original maiores que n.
    list, int -> list'''
    
    lista_com_n = lista.insert([0],n)
    lista_oredenada = lista.sort()
    i = lista.index(n)
    listanova = del(lista[i:])
    return listanova