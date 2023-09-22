def fatorial(numero):
    '''Recebe um número natural, e calcula o fatorial dele.

    int -> int'''

    fatorialNum = 1
    
    while numero > 0:
        fatorialNum = fatorialNum*numero
        numero = numero - 1
    return fatorialNum