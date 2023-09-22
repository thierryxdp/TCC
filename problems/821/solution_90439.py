def fatorial (numero):
    '''
    função que dado um número, calcula o fatorial deste número
    int-->int
    '''

    fatorial = 1
    num_anteriores = 1

    while num_anteriores<= numero:
        fatorial = fatorial * num_anteriores
        num_anteriores = num_anteriores + 1

    return fatorial