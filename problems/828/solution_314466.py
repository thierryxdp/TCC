def primo(n):
    '''Recebe um número natural e identifica se
    ele é primo ou não; int -> bool'''
    n_divisores = []
    for i in range (1,n+1):
        if n % i == 0:
            n_divisores += [i]
    if len(n_divisores) == 2:
        return True
    else:
        return False