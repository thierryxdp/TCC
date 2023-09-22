def fatorial (n):
    """Função que dado um número é calculado o fatorial deste número"""
    """int -> int"""
    
    num = 1
    
    while n >= 1:
        num = num * n
        n = n-1
    return num