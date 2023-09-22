def soma_h(n):
    '''Calcula e retorna o valor H com N termos.
    int -> float'''
    soma = 0
    for i in range(1, n+1):
        h = 1/i
        soma += h
    return round(soma, 2)