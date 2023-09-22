import math
def primo(n):
    '''
    Recebe um inteiro n e retorna um bool dizendo se n é primo ou não
    
    int -> bool
    '''
    for d in range(2,math.floor(math.sqrt(n))+1):
        if n%d==0:
            return False
    return True