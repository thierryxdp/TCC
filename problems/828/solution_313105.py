def primo(n):
    '''Retorna se o numero n e primo ou nao
    int -> bool'''
    n_divisores = 0
    for possibilidades in range(n):
        if n%(possibilidades+1) == 0:
        	n_divisores += 1
    return n>2