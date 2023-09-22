def maiores(lista_de_numeros: list,n: int) -> list:
    """ dado uma lista de números inteiros e um número inteiron,
    retorna outra lista, que contenha todos os números da lista original
    maiores que n. """
    
    list.append(lista_de_numeros, n)
    list.sort(lista_de_numeros)
    del lista_de_numeros[:list.index(lista_de_numeros,n)]
    
    if list.index(lista_de_numeros,n) == 0:
        list.remove(lista_de_numeros, n)
    

    return lista_de_numeros