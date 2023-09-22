def fatorial(numero):
    '''função que calcula o fatorial de um dado número
    int -> int'''
    num = 1
    while numero >= 1:
        num = num * numero
        numero = numero - 1
    return num