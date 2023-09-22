def insere(lista_numero,n):
    """ Essa função vai receber como parâmetro de entrada
    uma lista ordenada (crescente) de números inteiros e um
    número inteiro n. Posto isso, essa função irá retornar 
    uma nova lista contendo a lista origal e o inteiro n, sen-
    do que, todos os números estarão postos em ordem crescen-
    te.
    
    list, int -> list
    """
    
    
    
    lista_1 = [n]
    lista_2 = lista_numero + lista_1
    list.sort(lista_2)
    
    return lista_2