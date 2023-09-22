def fatorial(numero):
    '''função que retorna o fatorial de um número
    int -> int'''
    resultado = 0
    while numero > 1:
        resultado = numero * (numero - 1)
        numero = numero - 1
    return resultado