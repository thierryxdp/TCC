def fatorial(n):
    """Calcula o fatorial desse número"""
    """int -> int"""
    
    fatorial = 0
    i = 1
    lista = list(range(1,n))
    while i < len(lista):
        fatorial *= lista[len(lista)-1] * lista[len(lista)-2]
        i = i + 1
    return fatorial