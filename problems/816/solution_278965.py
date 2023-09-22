def maiores(lista,n):
    '''Função que dada uma lista e um numero inteiro retorna outra lista
    com os numeros maiores que n da lista original
    list, int -> list'''
    list.append(lista,n)
    list.sort(lista)
    a= list.index(lista, n)
    return lista[a+1:]