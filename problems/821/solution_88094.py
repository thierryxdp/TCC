def fatorial(n):
    """Calcula o fatorial desse número"""
    """int -> int"""
    
    fatorial = 0
    i2=1
    i = 0
    lista = list(range(1,n))
    while i < len(lista):
        fatorial += lista[i2-1] * lista[i2]
        i2 = i2+1
        i = i + 1
    return fatorial