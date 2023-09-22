import math    
def primo(n):
    '''Função que  calcula e retorna se o número é primo ou não.int->bool'''
    if n == 2:
        return True
    if n % 2 == 0 or n<= 1:
        return False
    r = int(math.sqrt(n)) + 1
    for divisor in range(3,r,2):
        if n % divisor == 0:
            return False
    return True