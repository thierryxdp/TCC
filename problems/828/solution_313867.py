def primo(n):
    '''Funcao que retorna se o numero de entrada e primo ou nao.
    int->bool'''
    div=range(2,n)
    for x in div:
        if n%x==0:
            return False
    return True