def primo(n):
    """Funcao que recebe um numero inteiro e retorna se ele e um numero primo ou nao. int=>bool"""
    primo=1
    x=1
    while x<n:
        if n%x==0:
            primo=primo+1
        x=x+1
    if primo>2:
        return False
    else:
        return True