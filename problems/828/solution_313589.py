def primo(n):
    '''Funcao que retorna se o numero de entrada e primo ou nao.
    int->bool'''
    x=range(1,n+1)
    z=2
    for y in x:
        if y%z==0:
            z=z+1
        return False
    else:
        return True