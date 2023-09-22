def repetidos(num):
    """ Insira uma lista de numeros e a funcao retornara o numero de vezes que um elemento
    da lista é igual ao elemento anterior"""
    n = 0
    r = 0
    while n+1 < len(num):
        if num[n] == num[n+1]:
            r += 1
            n += 1
    return r