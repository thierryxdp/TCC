def fatorial(numero):
    '''Calcula a fatorial de um número
    entrada: int
    saída: int
    '''
    total=numero
    while numero>1:
        numero=numero-1
        total= total*numero
    return total