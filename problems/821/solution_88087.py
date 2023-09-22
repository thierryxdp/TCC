def fatorial(n):
    """Calcula o fatorial desse número"""
    """int -> int"""
    
    fatorial = 0
    i = 0
    i2=0
    lista = list(range(1,n))
    while i < len(lista):
        fatorial += lista[len(lista)] * lista[len(lista)-1]
        
        i = i + 1
    return fatorial