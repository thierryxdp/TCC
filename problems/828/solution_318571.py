def primo(n):
    '''A função retorna se o número fornecido é primo ou não
    int -> bool'''
    i = 2
    while i<n:
        if n%i == 0:
            return False
        i = i+1
    return True