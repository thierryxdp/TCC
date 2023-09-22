import math
def primo(n):
    '''Função que calcula e retorna true se o numero dado na entrada n
    for primo e false caso contrário
    int -> bool'''
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    r = int(math.sqrt(n))+1
    for d in range (3,r,2):
        if n % d == 0:
            return False
    return True