def maiores(lista_numero, n):
    '''Funcao que recebe uma lista com numeros
    inteiros e um numero inteiro (n), e retorna
    uma nova lista com os inteiros maiores que (n).
    Dados de entrada: list, int
    Valor de saida: list
    '''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    posicao_de_n = list.index(lista_numero, n)
    lista_maiores_que_n = list(range(posicao_de_n + 1, lista_numero[-1] + 1))
    return lista_maiores_que_n