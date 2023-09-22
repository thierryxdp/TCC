import math
def primo(n):
    '''Retorna se n é primo ou não'''
    for i in range(2, math.ceil(n**(1/2)) + 1 ):
        if n%i==0:
            return False
    else:
        return True