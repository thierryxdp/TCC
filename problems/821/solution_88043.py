def fatorial(y):
    """Dado um número, retorna seu fatorial;
    int -> int"""
    x = list(range(1,y+1))
    a = 0
    resultado = 1 
    while a < len(x) :
        resultado = x[a] * resultado
        a = a + 1 
    
    return resultado