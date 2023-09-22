def fatorial(numero):

    '''essa função calcula o fatorial de um determinado numero

    int -> int'''

    multiplicacao = 1

    for i in range(1, (numero+1)):

        multiplicacao = multiplicacao * i  

    return multiplicacao