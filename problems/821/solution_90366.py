def fatorial (numero: int)-> int:
    '''Retorna o fatorial do numero dado'''
    i = numero - 1
    while i > 0:
        numero = numero * i
        i = i - 1
    return numero