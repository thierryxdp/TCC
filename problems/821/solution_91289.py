def fatorial(numero):
    '''
    Função que dado um número, retorna seu fatorial.
    int->int
    '''

    x = 0
    fat = 1
    num = numero
    while i < numero:
        fat = fat * num
        num = num - 1
        x = x + 1
    return fat