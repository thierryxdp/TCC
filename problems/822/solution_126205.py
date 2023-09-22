def repetidos(num):
    """ Insira uma lista e a funcao retornara o numero de vezes que um elemento da lista é
    igual ao elemento anterior"""
    n = 0
    resposta = 0
    L = len(num)
    while n+1 < L:
        if num[n] == num[n+1]:
            resposta += 1
            n += 1
    return r