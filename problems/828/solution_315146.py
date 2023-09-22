from math import sqrt
def primo(numero):
    """Dado um número qualquer, retorna se ele é primo ou não:
    int-->bool"""
    for primo in range(1,int(sqrt(numero))):
        if (numero%primo==0) and primo!=numero:
            return False
    return True