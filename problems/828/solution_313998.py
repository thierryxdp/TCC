def primo(x):
    '''Verifica se um número é primo ou não.
    int -> bool'''
    n=2
    for i in range(x-1):
        if (x%n)==0:
            return False
        n=n+1
    return True