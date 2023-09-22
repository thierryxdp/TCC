def insere(lista_numero,n):
    '''
    dado uma lista ordenada de maneira crescente de numeros
    inteiros e um numero inteiro n, retorna a mesma lista
    com n incluso e ainda ordenada de maneira crescente
    dados de entrada: list, int
    retorna: list
    '''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero