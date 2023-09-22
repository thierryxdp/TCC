def fatorial(numero):
    '''Calcula a fatorial de um número;
    int -> int'''
    multiplicador = 2
    num_anterior = 1
    while multiplicador <= numero:
          num_anterior = num_anterior * multiplicador
          multiplicador = multiplicador + 1
    return num_anterior