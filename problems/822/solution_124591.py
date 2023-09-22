def repetidos(lista_de_n):
    '''Função que recebe de entrada uma lista de numeros e retorna o numero de vezes que um elemento da lista é igual ao anterior'''
    '''list -> int'''
    i = 0
    n_repetidos = []
    while i < len(lista_de_n) - 1:
        if lista_de_n[i] == lista_de_n[i + 1]:
            list.append(n_repetidos, lista_de_n)
        i += 1
    return len(n_repetidos)