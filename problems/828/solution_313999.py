def primo(x):
    '''Verifica se um número é primo ou não.
    int -> bool'''
    n=2
    for i in range(x):
        if (x%n)==0 and x!=n:
            return False
        n=n+1
    return True