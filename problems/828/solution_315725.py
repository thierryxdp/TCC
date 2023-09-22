import math
def primo(num):
    '''calcule uma funcao que dado um numero inteiro positivo, retorne
    se esse é primo ou não em forma de valor booleano. int-->bool.'''
    raiz = int(math.sqrt(num)) + 1
    for i in range(3,raiz,2):
        if num % i == 0:
            return False
    return True