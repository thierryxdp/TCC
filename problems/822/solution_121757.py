def repetidos(lista_numeros:list)->int:

    """ Função que tem como entrada uma lista de núumeros, e retorne a quantidade
        de vezes que um elemento da lista é igual ao elemento anterior.

    """


    n = 1
    contador = 0

    while n<len(lista_numeros):

        if lista_numeros[n] == lista_numeros[(n-1)]:

            contador = contador + 1
            
        n += 1

    return contador