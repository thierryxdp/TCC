def primo(n):
    """Dado um número n, diz se ele é primo ou não"""
    
    for divisor in range(n,1,-2):
        if n % 2 == 0:
            return False
        elif n % divisor ==0:
            return False
        else:
            return True