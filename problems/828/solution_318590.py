def primo(x):
    '''retorna true se um numero inteiro x de 
    entrada for primo e false se nao for
    int -> bool'''
    if x >= 2:
        for i in range( 2, x ):
            if not ( x % i ):
                return False
    else:
        return False

    return True