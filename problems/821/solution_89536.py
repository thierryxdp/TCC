def fatorial(n):
    """Função que calcula o fatorial de um numero n"""
    """int->int"""
    x=[n]
    i=0
    while i<n:
        x=[x+n-i]
        i=i+1
    return x