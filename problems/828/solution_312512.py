from math import *
def primo(n):
    """Dado um número inteiro positivo, retorna se este é primo ou não. int ->bool."""
    for i in range(2,round(sqrt(n)+1)):
        if n%i == 0:
            return False
    return True