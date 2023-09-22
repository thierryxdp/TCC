def maiores(lista_numeros, n):
    '''Função que recebe um número inteiro e uma lista de
    números inteiros e retorna uma nova lista com os números
    maiores que n.
    [list], int -> [list]'''
    if n in lista_numeros:
        lista_numeros = lista_numeros + [n]
    	list.sort(lista_numeros)
    	lista_final = lista_numeros[list.index(lista_numeros, n) + 2: ]
        return lista_final
    else:
        lista_numeros = lista_numeros + [n]
    	list.sort(lista_numeros)
    	lista_final = lista_numeros[list.index(lista_numeros, n) + 1: ]
        return lista_final