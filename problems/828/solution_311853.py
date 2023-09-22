def primo(n):
    '''Retorna True se o numero for primo e falso se não for.
       int -> bool'''
    divisores = []
    for i in range(2,n):
        if n%i == 0:
            divisores += ['sim']
        else:
            divisores += ['não']
    if 'sim' in divisores:
        return False
    else:
        return True