import math
def primo(n):
    '''Escreva um numero natural. A funcao retorna True caso seja primo e
    False caso NAO seja.
    int -> bool'''
    maximo_div=math.floor(math.sqrt(n))
    for x in range(2,maximo_div+1):
        if n%x==0:
            return False
        else:
            return True