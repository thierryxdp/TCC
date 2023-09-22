def maiores(lista,n):
    '''Retorna uma lista com os numeros da lista original maiores que n
    list, int -> list'''
    lista.append(n)
    lista.sort()
    corte=list.index(lista,n)
    listafinal=lista[corte+1:]
    return listafinal