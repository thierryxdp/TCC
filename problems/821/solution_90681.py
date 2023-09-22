def fatorial(numero):
    '''
    dado um numero como argumento, calcula seu fatorial
    dados de entrada: int
    retorna: int
    '''
    contador = numero - 1
    fatorial_numero = numero
    while contador > 1:
        fatorial_numero = fatorial_numero * contador
        contador = contador - 1
    return fatorial_numero