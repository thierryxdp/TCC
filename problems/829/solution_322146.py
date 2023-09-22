def soma_h(n):
    '''Recebe um número e retorna o valor H resultado da equação dada, int->float'''
    H=1
    for divisor in range(n+1):
        if dividor !=0:
            H=H+(1/divisor)
    return round(H,2)