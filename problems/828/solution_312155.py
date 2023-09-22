from math import ceil, sqrt

def primo(n):
    limite = ceil(sqrt(n))
    for i in range(2, limite + 1):
        if n % i == 0:
            return False
    
    return True