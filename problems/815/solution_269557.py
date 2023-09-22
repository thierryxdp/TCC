def insere(lista_numero, n):
    """ Funcao que recebe um lista ordenada (crescente) de numeros inteiros e um numero inteiro n.
    	Retorna uma nova lista ordenada (crescente) com o numero n
    """
    lista_numero.append(n)
    lista_numero.sort()
    
    return lista_numero