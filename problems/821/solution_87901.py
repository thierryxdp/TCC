def fatorial(numero):
    '''função que retorna o fatorial de um número
    int -> int'''
    resultado = 1
    while numero > 1:
        resultado = resultado * numero * (numero - 1)
        numero -= 1
    return resultado