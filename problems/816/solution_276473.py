def maiores(lista_numero, n):
    '''função que dado uma lista de números inteiros e um número inteiro n, retorna
    uma nova lista, que contenha todos os números da primeira lista maiores que n
    list, int ->'''
    lista = lista_numero + [n]
    list.sort(lista)
    a = list.index(lista,n)
    b = list.count(lista,n)
    return lista[a + b:]