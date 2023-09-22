def primo(n):
    '''
    A função identifica se um número é primo ou não
    retornando um bool
    '''
    i = 0
    for x in range(1, 100):
        if n % x == 0:
            i += 1
    if i == 2:
        return True
    else:
        return False