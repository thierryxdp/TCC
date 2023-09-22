def fatorial(n):
    """Calcula o fatorial desse número"""
    """int -> int"""
    
    fatorial = 1
    i = 0
    lista = list(range(1,n))
    while i+1 < len(lista):
        fatorial *= lista[::-1][i] * lista[::-1][i+1]
        i = i + 1
    return fatorial