def maiores(lista, n):
    '''Dada uma lista e um numero inteiro, a funçao retorna uma lista
       contendo todos os numeros da lista original maiores que n
       list, int -> list'''
    list(lista)
    lista = lista.insert(0, n)
    lista = sorted(lista)
    indice = find(n, lista)
    qntdmaiores = lista[indice+1:]
    return list(qntdmaiores)