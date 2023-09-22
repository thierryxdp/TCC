def filtra_pares(tupla_int):
    """ Dada uma tupla com quatro elementos inteiros como parâmetro,
    retorna uma nova tupla contendo apenas os elementos pares da tupla
    original, na mesma ordem que se encontravam.
    tuple -> tuple"""
    
    tupla_int = a,b,c,d
    A = a / 2 # o último algarismo vale 0 para par e 5 para ímpar
    B = b / 2 # o último algarismo vale 0 para par e 5 para ímpar
    C = c / 2 # o último algarismo vale 0 para par e 5 para ímpar
    D = d / 2 # o último algarismo vale 0 para par e 5 para ímpar
    
    if A[-1] == 5:
        a = None
    else:
        a = a
    if B[-1] == 5:
        b = None
    else:
        b = b
    if C[-1] == 5:
        c = None
    else:
        c = c
    if D[-1] == 5:
        d = None
    else:
        d = d
    return (a,b,c,d)