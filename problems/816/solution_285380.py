def maiores(lista_numero, n):
	'''
    	Funcao que recebe uma lista de numeros inteiros e um
        numero inteiro n e retorna outra lista ordenados em
        ordem crescente
        list, int -> list
    '''
    if n in lista_numero:
        list.sort(lista_numero)
        lista_n = lista_numero[list.index(lista_numero, n) + 1:]
        return lista_n
    
    else:
        lista_numero.insert(-1, n)
        list.sort(lista_numero)
        lista_n = lista_numero[list.index(lista_numero, n) + 1:]
        return lista_n