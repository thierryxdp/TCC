def soma_h(n):
    '''Recebe um número e retorna o valor H resultado da equação dada, int->float'''
    H=0
    for divisor in range(n+1):
        if divisor!=0:
            H=H+(1/divisor)
    return round(H,2)