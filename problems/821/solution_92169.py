def fatorial(numero):
    '''recebe um numero e retorna o fatorial desse numero'''
    proximo = numero - 1
    
    while proximo > 0:
        valor = numero * proximo
        numero = valor
        proximo = proximo - 1

    return numero