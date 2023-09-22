def fatorial(n):
    '''Recebe um número n e retorna o seu fatorial (int -> int'''
    resultado = 1 
    numero = n
    while numero > 0:
        resultado = resultado * numero 
        numero = numero - 1
    return resultado