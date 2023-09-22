def fatorial(n):
    """Funcao que dado um numero n, calcula e retorna o 
    fatorial deste numero;
    int->int"""
    
    L=list(range(1,n+1))
    
    return numpy.prod(L)