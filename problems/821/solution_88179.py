def fatorial (n):
    """função que calcula e retorna o fatorial de n,através do dado de entrada n;
    Entrada: int
    Saída: int"""
    a = list(range(1,n + 1))
    b = 1
    c = a[0]
    
    while b < len(a):
        c = c * a[b]
        b = b + 1
    return c