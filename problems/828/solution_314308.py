import math

def primo(n):
    """Função que retorna se um número n é primo ou não."""
    """ Int -> Boolean"""
    if n >= 2:
        for numeros in range(2,n):
            if (n%math.floor(math.sqrt(numeros))) == 0:
                return True
            else:
                return False