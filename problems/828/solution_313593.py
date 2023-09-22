def primo(n):
    '''Funcao que retorna se o numero de entrada e primo ou nao.
    int->bool'''
    x=range(1,n+1)
    for y in x[2:n]:
        if n%y==0:
    		return False
        if n%y!=0:
            return True