def insere(lista_numero, n):
    '''
    	A função insere um número n em uma lista contendo outros número em ordem
        crescente de forma que n seja adicionado no lugar correto, mantendo a ordem
        da lista anterior.
        lista_numero -> list (lista contendo números em ordem crescente)
        n -> float
        list, float -> list
    '''
    lista_numero.append(n)
    lista_numero.sort()
    
    return lista_numero