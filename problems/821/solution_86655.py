def fatorial(num):
    """Função que calcula o fatorial do número de entrada. int -> int"""
    r = 1
    c = 1

    while c <= num:
        r = r * c
        c = c + 1
    
    return r