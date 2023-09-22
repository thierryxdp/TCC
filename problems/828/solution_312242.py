import math
def primo(n):
    '''Escreva um numero natural. A funcao retorna True se o num for primo,
    e False caso nao seja.
    int -> bool'''
    if n==1:
        return False
    elif n==2:
        return True
    elif n>2 and n%2==0:
        return False
    else:
        max_div=math.floor(math.sqrt(n))
        for x in range(3,max_div+1,2):
            if n%x==0:
                return False
        return True