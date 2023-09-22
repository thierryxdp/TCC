def repetidos(num_lista):
    '''Função que receba uma lista de números, num_lista, e que retorna
    a quantidade de vezes que um elemento da lista é igual ao elemento anterior.
    list=>int'''
    indice = 1
    n_vezes = 0
    while indice < len(num_lista):
        if num_lista[indice-1] == num_lista[indice]:
            n_vezes += 1
        indice += 1
    return n_vezes