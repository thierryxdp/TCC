from math import sqrt
def primo(numero):
    """Dado um número qualquer, retorna se ele é primo ou não:
    int-->bool"""
    for primo in range(2,int(sqrt(numero)+1)):
        if numero%primo==0:
            return False
    return True