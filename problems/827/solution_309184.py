def qtd_divisores(numero):
    '''recebe um numero e retorna a quantidade de
    divisores desse numero.
    float -> int
    '''
    quantidade = 0
    for n in range(1,numero + 1):
        if numero%n == 0:
            quantidade += 1
    return quantidade