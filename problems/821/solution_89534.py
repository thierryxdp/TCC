def fatorial(n):
    """Função que, dado um número, calcula o fatorial deste número; int->int"""
    
    fatorial = 1
    
    while n != 0:
        fatorial = fatorial*n
        n = n-1
    return fatorial