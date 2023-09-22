from math import sqrt
def primo(n):
    '''Verifica se um número é primo ou não;
int -> bool'''
    for i in range(2, int(sqrt(n)) + 1):
        if n%i==0:
            return False
    return True