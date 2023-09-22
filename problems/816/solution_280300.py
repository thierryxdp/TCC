def maiores(lista,n):
    ''' função que dada uma lista de números inteiros
    e um número inteiro n, retorna outra lista contendo todos
    os números da lista original maiores que n. list, int -> list'''
    lista.append(n)
    list.sort(lista)
    a = list.index(lista,n)
    return lista[a + 1:]