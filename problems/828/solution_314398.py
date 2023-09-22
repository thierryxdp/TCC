def primo(n):
    """Dado um número n, diz se ele é primo ou não"""
    divisores= []
    
    for divisor in range(3,n,2):
        if n % 2 == 0:
            return False
        elif n % divisor == 0:
            return False
    return True