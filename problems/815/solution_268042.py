def insere (lista_numero, n):
    '''Funcao que, dada uma lista ordenada (crescente) de numeros inteiros e um numero inteiro n, inclua n na lista de forma que a mesma continue ordenada.
    list, int -> list'''
	
    lista = lista_numero
    lista_numero.append (n)
    list.sort (lista)
    return lista