def insere(lista_numero, n):
    ''' função que recebe uma lista ordenada (crescente) de números inteiros e um número inteiro n, e inclui n na lista de tal maneira que continue ordenada;
	list, int -> list '''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero