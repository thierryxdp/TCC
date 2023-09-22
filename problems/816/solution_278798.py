def maiores (lista_numeros, n) :
    """Funcao que recebe uma lista de numeros inteiros e um numero inteiro n e retorna outra lista contendo todos os numeros da lista original maiores que n"""
    list.append(lista_numeros, n)
    list.sort(lista_numeros)
    n = list.index(lista_numeros,n)
    lista_numeros = lista_numeros[n:]
    del lista_numeros[0]
    return lista_numeros