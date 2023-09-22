def primo(n):
    '''verifica se o número é primo
    int -> bool'''
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    else:
        return True