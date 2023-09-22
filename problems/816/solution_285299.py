def maiores(lista_inteiros, n):
    '''Esta funcao recebe uma lista de numeros inteiros e um numero inteiro n, e retorna outra lista, contendo todos os numeros maiores que n, em ordem crescente.'''
    '''list, int --> list'''
    list.append(lista_inteiros, n)
    list.sort(lista_inteiros)
    list.index(lista_inteiros, n)
    lista_dos_maiores_que_n = lista_inteiros[(n - 1):]
    return lista_dos_maiores_que_n