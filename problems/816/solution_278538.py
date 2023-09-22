def maiores(lista,n):
    """ essa função irá retornar todos os numeros da lista original maiores que n
    entrada -> lista, int
    saida -> lista """
    list.append(lista, n)
    list.sort(lista)
    numero = list.index(lista, n)
    del lista[0:numero+1]
    return lista