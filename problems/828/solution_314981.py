import math
def primo(num):
    '''
        dado um inteiro num, retorna se o número é primo ou não.
        int -> bool
    '''
    div=1
    for n in range(1,math.ceil(num/2)):
        if num % n == 0:
            div=div+1
    if div != 2:
        return False
    else:
        return True