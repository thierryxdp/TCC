def insere (lista_numero,n):
    """ A função insere, dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclue n na posição correta, ou seja, de tal maneira que a lista continue ordenada.
        
        Parameters:
            lista_numero = lista em ordem crescente a ser análisada
            n = numero a ser inserido na lista de forma que ela continue a ser crescente 

        Testes:
            insere([1,2,4,5],3) = [1, 2, 3, 4, 5]
            insere([1,2,3,4,5],3) = [1, 2, 3, 3, 4, 5]

        Returns:
            lista em ordem crescente já com o numero a ser inserido nela
            list, int --> list
    """
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero