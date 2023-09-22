def maiores(lista,n):
    '''função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n.
    entrada: list
    saída: list'''
    list.append(lista,n)
    list.sort(lista)
    var1 = str.index(lista,n)
    var2 = var1 + 1
    return lista[var2: ]