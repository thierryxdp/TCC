import math    
def primo(numero):
    '''Função que verifica se o número é primo ou não.'''
    '''int->bool'''
    if numero == 2:
        return True
    if numero % 2 == 0 or numero <= 1:
        return False
    raiz = int(math.sqrt(numero)) + 1
    for divisor in range(3,raiz,2):
        if numero % divisor == 0:
            return False
    return True