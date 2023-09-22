def primo(n):
    '''Funcao retorna se um numero e primo
    int -> boolean
    '''
    r = 0
    for x in range(1,n+1):
        if n % x == 0:
            r += 1
    if r == 2:
        return True
    else:
        return False