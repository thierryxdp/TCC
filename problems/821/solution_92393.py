def fatorial(n):
    '''Calcula o fatorial do número de entrada.
Assinatura: int -> int
Casos de teste:
fatorial(5) == 120
fatorial(4) == 24
fatorial(10) == 3628800
'''
    for i in list(range(1, n)):
        n *= i
    return n