def fatorial(numero):
    """Recebe um número e calcula o fatorial desse número;
    int -> int"""
    fatorial = 1
    i = 1
    while i <= numero:
        fatorial *= i
        
    return fatorial