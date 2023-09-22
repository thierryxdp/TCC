def primo(x):
    '''Verifica se um número é primo ou não.
    int -> bool'''
    i=2
    for i in range(x):
        if (x%i)==0:
            return False
        i=i+1
    return True